#!/usr/bin/env python3
"""Lint the seo-kit knowledge base and skills against knowledge/conventions.md.

Checks plugins/seo-kit/knowledge/**/*.md and plugins/seo-kit/skills/**/*.md and prints
`path:line: RULE: message`. Exit 1 if any error (warnings do not fail unless
--warnings-as-errors). conventions.md is the source of truth for the prefix table.

Rules
  K001 audit table header must be exactly | ID | Check | How to verify | Severity | Source |
  K002 IDs unique across files; alias rows must point to an existing ID in another file
  K003 ID prefix matches the file (prefix table of conventions.md)
  K004 Severity in {Critical, High, Medium, Low}
  K005 warning sign only on deprecated / unsupported checks
  K006 required sections of topic files; site-type notes in the fixed order
  K007 forbidden strings (personal data, private paths)
  K008 legacy archetype slugs only where allowed
  K009 (warning) future tense next to a date that is already past
  K010 first line after the H1 of a topic file starts with "> Updated 20"
  K011 (warning) untranslated Italian heuristic
  K012 every [G] source tag carries an https link

Usage: python tools/check_knowledge.py [--root PATH] [--warnings-as-errors] [--only K001,K005]
Standard library only, Python 3.9+.
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index as bi  # noqa: E402  (shared parsing helpers)

WARNING_RULES = {"K009", "K011"}
SEVERITIES = {"Critical", "High", "Medium", "Low"}
EXEMPT_TOPIC = {"archetypes.md", "conventions.md", "myths-deprecated.md", "INDEX.md"}
REQUIRED_SECTIONS = [
    "Facts and rules (Google)",
    "Audit checks",
    "Build rules",
    "Third-party views",
    "Myths and outdated advice",
]
SITE_TYPE_ORDER = ["ecommerce", "editorial", "local-business", "personal-brand", "professional-services", "saas-product"]
SITE_TYPE_ALIASES = {"e-commerce": "ecommerce"}
WARN_ALLOWED = ("deprecated", "retired", "unsupported", "do not", "not supported")
FORBIDDEN = ["eliaraguso", "bilancio di competenze", "orientatrice", "orientamento", "raguso", "verona", "carrara"]
ALLOWED_PHRASES = ["Studio Ferri Orientamento"]  # fictional example entity of conventions.md
SOURCES_PATH_RE = re.compile(r"(?<![\w-])sources/", re.I)
URL_RE = re.compile(r"https?://\S+", re.I)
LEGACY_SLUGS_RE = re.compile(r"(?<![\w-])(professionista-servizi|attivita-locale|editoriale|prodotto-saas)(?![\w-])")
MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
    "gennaio": 1, "febbraio": 2, "marzo": 3, "aprile": 4, "maggio": 5, "giugno": 6, "luglio": 7, "agosto": 8,
    "settembre": 9, "ottobre": 10, "novembre": 11, "dicembre": 12,
}
FUTURE_RE = re.compile(r"(?<![\w-])(will be|will stop|until|entro|dal) .{0,40}?(20\d\d)(?!\d)", re.I)
ITALIAN_RE = re.compile(r"(?<!\w)(della|degli|delle|perché|è)(?!\w)", re.I)
G_TAG_RE = re.compile(r"\[G(?: OH [^\]\s]+)?\]")


class Finding:
    def __init__(self, path, line, rule, message):
        self.path, self.line, self.rule, self.message = path, line, rule, message

    @property
    def is_warning(self):
        return self.rule in WARNING_RULES

    def __str__(self):
        tag = "warning: " if self.is_warning else ""
        return "%s:%d: %s: %s%s" % (self.path, self.line, self.rule, tag, self.message)


def mask_code_spans(line):
    """Blank out inline code spans (keeps length so columns stay aligned)."""
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)


class Linter:
    def __init__(self, root, today=None):
        self.root = Path(root)
        self.today = today or datetime.date.today()
        self.kdir = bi.knowledge_dir(self.root)
        self.sdir = self.root / "plugins" / "seo-kit" / "skills"
        self.findings = []
        self.ids = {}  # id -> (relpath, line, is_alias)
        self.alias_rows = []  # (relpath, line, id, target)

    # ---- plumbing
    def rel(self, path):
        try:
            return Path(path).relative_to(self.root).as_posix()
        except ValueError:
            return Path(path).as_posix()

    def add(self, path, line, rule, message):
        self.findings.append(Finding(self.rel(path), line, rule, message))

    def files(self):
        out = []
        for base in (self.kdir, self.sdir):
            if base.is_dir():
                out.extend(sorted(base.rglob("*.md")))
        return out

    def is_topic_file(self, path):
        return path.parent == self.kdir and path.name not in EXEMPT_TOPIC

    # ---- run
    def run(self):
        conv = self.kdir / "conventions.md"
        if not conv.is_file():
            raise SystemExit("error: %s not found" % conv)
        prefixes = bi.parse_prefix_table(conv)
        if not prefixes:
            raise SystemExit("error: no prefix table found in %s" % conv)
        self.file_prefix = {f: p for p, f in prefixes}
        for path in self.files():
            text = bi.read_text(path)
            lines = list(bi.iter_lines(text))
            self.check_tables(path, lines)
            self.check_forbidden(path, lines)
            self.check_legacy_slugs(path, lines)
            self.check_future(path, lines)
            self.check_italian(path, lines)
            self.check_g_links(path, lines)
            if self.is_topic_file(path):
                self.check_sections(path, text)
                self.check_updated_line(path, lines)
        self.check_ids_global()
        return self.findings

    # ---- K001-K005 (+ collect IDs for K002)
    def check_tables(self, path, lines):
        if path.name == "INDEX.md" and path.parent == self.kdir:
            return  # generated by build_index.py with its own header; never hand-linted
        table = None  # None or dict(header_ok, header_line)
        for n, line, in_fence in lines:
            if in_fence:
                table = None
                continue
            cells = bi.split_row(line)
            if cells is None:
                table = None
                continue
            if table is None:
                if cells and cells[0] == "ID":
                    ok = cells == bi.CHECK_HEADER
                    if not ok:
                        self.add(path, n, "K001", "audit table header must be exactly '| %s |', found '| %s |'"
                                 % (" | ".join(bi.CHECK_HEADER), " | ".join(cells)))
                    table = {"ok": ok}
                else:
                    table = {"ok": None}  # not an audit table
                continue
            if table["ok"] is not True or bi.is_separator(cells):
                continue
            self.check_row(path, n, cells)

    def check_row(self, path, n, cells):
        if len(cells) != 5:
            self.add(path, n, "K001", "audit row has %d cells, expected 5" % len(cells))
            return
        cid, check, _how, sev, _src = cells
        # K003: ID shape and prefix
        if not bi.ID_RE.match(cid):
            self.add(path, n, "K003", "malformed check ID %r (expected two capital letters, dash, number)" % cid)
        else:
            expected = self.file_prefix.get(path.name)
            if path.parent != self.kdir or expected is None:
                self.add(path, n, "K003", "%s: check IDs are only defined in knowledge/ files with a prefix registered in conventions.md (%s)" % (cid, path.name))
            elif cid.split("-")[0] != expected:
                self.add(path, n, "K003", "%s: prefix must be %s in %s" % (cid, expected, path.name))
        # K004
        if sev not in SEVERITIES:
            self.add(path, n, "K004", "%s: severity %r is not one of Critical, High, Medium, Low" % (cid, sev))
        # K005
        row_text = " ".join(cells)
        if "⚠" in row_text and not any(w in check.lower() for w in WARN_ALLOWED):
            self.add(path, n, "K005", "%s: warning sign on a check that is not deprecated/unsupported; "
                     "use a 'Caveat:' sentence instead" % cid)
        # K002 bookkeeping
        m = bi.ALIAS_RE.match(check)
        target = m.group(1) if m else None
        rel = self.rel(path)
        if cid in self.ids:
            prev = self.ids[cid]
            self.add(path, n, "K002", "duplicate ID %s (first defined at %s:%d)" % (cid, prev[0], prev[1]))
        else:
            self.ids[cid] = (rel, n, target is not None)
        if target:
            self.alias_rows.append((rel, n, cid, target))

    def check_ids_global(self):
        for rel, n, cid, target in self.alias_rows:
            hit = self.ids.get(target)
            if hit is None:
                self.findings.append(Finding(rel, n, "K002", "%s is an alias of %s, which does not exist" % (cid, target)))
            elif hit[0] == rel:
                self.findings.append(Finding(rel, n, "K002", "%s is an alias of %s in the same file; aliases must point to another file" % (cid, target)))
            elif hit[2]:
                self.findings.append(Finding(rel, n, "K002", "%s is an alias of %s, which is itself an alias; point to the owning ID" % (cid, target)))

    # ---- K006
    def check_sections(self, path, text):
        heads = [(n, t) for n, lvl, t in bi.parse_headings(text) if lvl == 2]
        titles = [t.strip() for _n, t in heads]
        for req in REQUIRED_SECTIONS:
            if req not in titles:
                self.add(path, 1, "K006", "missing required section '## %s'" % req)
        for n, t in heads:
            if t.strip() == "Notes by site type":
                self.check_site_type_order(path, text, n)

    def check_site_type_order(self, path, text, start):
        last_idx, last_name = -1, None
        in_section = False
        for n, line, in_fence in bi.iter_lines(text):
            if n == start:
                in_section = True
                continue
            if not in_section or in_fence:
                continue
            if re.match(r"^##\s", line):
                break
            m = re.match(r"^\s*(?:[-*+]\s+)?\*\*([^*]+?)\*\*", line)
            if not m:
                continue
            label = re.sub(r"[^a-z0-9]+", "-", m.group(1).lower()).strip("-")
            label = SITE_TYPE_ALIASES.get(label, label)
            if label not in SITE_TYPE_ORDER:
                continue
            idx = SITE_TYPE_ORDER.index(label)
            if idx == last_idx:
                self.add(path, n, "K006", "site type '%s' appears twice in 'Notes by site type'" % label)
            elif idx < last_idx:
                self.add(path, n, "K006", "site type '%s' comes after '%s'; fixed order is %s"
                         % (label, last_name, " > ".join(SITE_TYPE_ORDER)))
            last_idx, last_name = max(idx, last_idx), label if idx >= last_idx else last_name

    # ---- K007
    def check_forbidden(self, path, lines):
        for n, line, _f in lines:
            work = line
            for phrase in ALLOWED_PHRASES:
                work = re.sub(re.escape(phrase), " " * len(phrase), work, flags=re.I)
            low = work.lower()
            hits = []
            for term in FORBIDDEN:  # longest first, masked so 'raguso' is not repeated inside 'eliaraguso'
                if term in low:
                    hits.append(term)
                    low = low.replace(term, " " * len(term))
            if SOURCES_PATH_RE.search(URL_RE.sub(lambda m: " " * len(m.group(0)), work)):
                hits.append("sources/")
            for h in hits:
                self.add(path, n, "K007", "forbidden string %r" % h)

    # ---- K008
    def check_legacy_slugs(self, path, lines):
        rel = self.rel(path)
        if path.name == "conventions.md" and path.parent == self.kdir:
            return
        if rel.endswith("skills/seo-discovery/SKILL.md"):
            return
        is_arch = path.name == "archetypes.md" and path.parent == self.kdir
        for n, line, _f in lines:
            m = LEGACY_SLUGS_RE.search(line)
            if not m:
                continue
            if is_arch and re.search(r"alias|legacy", line, re.I):
                continue
            self.add(path, n, "K008", "legacy slug %r is only allowed in conventions.md, the alias line of archetypes.md "
                     "and skills/seo-discovery/SKILL.md" % m.group(1))

    # ---- K009
    def check_future(self, path, lines):
        for n, line, in_fence in lines:
            if in_fence:
                continue
            for m in FUTURE_RE.finditer(line):
                year = int(m.group(2))
                if year < self.today.year:
                    past = True
                elif year == self.today.year:
                    month = self._month_near(m.group(0), line[m.end():m.end() + 3])
                    past = month is not None and month < self.today.month
                else:
                    past = False
                if past:
                    self.add(path, n, "K009", "future-tense wording near a date that has already passed: %r" % m.group(0))

    @staticmethod
    def _month_near(matched, after):
        found = None
        for w in re.findall(r"[A-Za-zÀ-ſ]+", matched):
            if w.lower() in MONTHS:
                found = MONTHS[w.lower()]
        if found is None:
            m = re.match(r"-(0[1-9]|1[0-2])", after)
            if m:
                found = int(m.group(1))
        return found

    # ---- K010
    def check_updated_line(self, path, lines):
        h1 = None
        for n, line, in_fence in lines:
            if not in_fence and re.match(r"^#\s+\S", line):
                h1 = n
                break
        if h1 is None:
            self.add(path, 1, "K010", "topic file has no H1")
            return
        for n, line, _f in lines:
            if n > h1 and line.strip():
                if not line.startswith("> Updated 20"):
                    self.add(path, n, "K010", "first line after the H1 must start with '> Updated 20'")
                return
        self.add(path, h1, "K010", "no '> Updated 20...' line after the H1")

    # ---- K011
    def check_italian(self, path, lines):
        count, first = 0, None
        for n, line, in_fence in lines:
            if in_fence:
                continue
            if ITALIAN_RE.search(mask_code_spans(line)):
                count += 1
                first = first or n
        if count:
            self.add(path, first, "K011", "%d line(s) look untranslated Italian (della/degli/delle/perché/è); first at this line" % count)

    # ---- K012
    def check_g_links(self, path, lines):
        for n, line, in_fence in lines:
            if in_fence:
                continue
            masked = mask_code_spans(line)
            for m in G_TAG_RE.finditer(masked):
                rest = line[m.end():]
                if not rest.startswith("("):
                    self.add(path, n, "K012", "source tag %s has no link; use %s(https://...)" % (m.group(0), m.group(0)))
                    continue
                end = rest.find(")")
                url = rest[1:end] if end != -1 else rest[1:]
                if not url.startswith("https://"):
                    self.add(path, n, "K012", "source tag %s must link to an https URL, found %r" % (m.group(0), url[:60]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=None, help="repo root (default: parent of tools/)")
    ap.add_argument("--warnings-as-errors", action="store_true")
    ap.add_argument("--only", default=None, help="comma-separated rule ids, e.g. K001,K005")
    ap.add_argument("--today", default=None, help="override today's date, YYYY-MM-DD (for tests)")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    root = Path(args.root) if args.root else bi.default_root()
    today = datetime.date.fromisoformat(args.today) if args.today else None
    findings = Linter(root, today).run()
    if args.only:
        wanted = {r.strip().upper() for r in args.only.split(",") if r.strip()}
        findings = [f for f in findings if f.rule in wanted]
    findings.sort(key=lambda f: (f.path, f.line, f.rule))
    for f in findings:
        print(f)
    errors = [f for f in findings if not f.is_warning or args.warnings_as_errors]
    warnings = [f for f in findings if f.is_warning]
    print("%d error(s), %d warning(s)" % (len([f for f in findings if not f.is_warning]), len(warnings)), file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
