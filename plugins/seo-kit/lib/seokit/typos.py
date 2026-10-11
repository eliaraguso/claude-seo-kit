"""Optional spelling heuristics, one JSON pack per language (typo_patterns/<lang>.json).

Packs apply only when the page language (or --lang) matches. There is no fallback
language: a page without a matching pack gets no typo check at all.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Optional

PACK_DIR = Path(__file__).resolve().parent / "typo_patterns"
_FLAGS = {"i": re.IGNORECASE, "m": re.MULTILINE}
_cache: dict = {}


def primary_language(lang: Optional[str]) -> Optional[str]:
    if not lang:
        return None
    primary = re.split(r"[-_]", lang.strip())[0].lower()
    return primary or None


def available_languages() -> list:
    return sorted(p.stem for p in PACK_DIR.glob("*.json"))


def load(lang: Optional[str]):
    """Compiled patterns [(regex, why)] for a language, or None when there is no pack."""
    primary = primary_language(lang)
    if not primary or not re.fullmatch(r"[a-z]{2,3}", primary):
        return None
    if primary in _cache:
        return _cache[primary]
    path = PACK_DIR / f"{primary}.json"
    if not path.is_file():
        _cache[primary] = None
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    compiled = []
    for item in data.get("patterns", []):
        flags = 0
        for ch in item.get("flags", ""):
            flags |= _FLAGS.get(ch, 0)
        compiled.append((re.compile(item["pattern"], flags), item["why"]))
    _cache[primary] = compiled
    return compiled


def find(page: dict, lang: Optional[str]):
    """Typo suspects in title, description, headings and visible text.

    Returns None when no pack applies (so callers can omit the key), else a list.
    """
    patterns = load(lang)
    if patterns is None:
        return None
    fields = {
        "title": page.get("title") or [],
        "meta_description": page.get("meta_description") or [],
        "headings": [h.get("text", "") for h in page.get("headings") or []],
        # One entry per text node when available, so that a word ending one element and
        # starting the next (menu "Contact", then H1 "Contact") is not a doubled word.
        "visible_text": page.get("text_blocks") or [page.get("visible_text") or ""],
    }
    found = []
    for field, values in fields.items():
        for value in values:
            for regex, why in patterns:
                for m in regex.finditer(value):
                    context = " ".join(value[max(0, m.start() - 40):m.end() + 40].split())
                    found.append({"field": field, "match": m.group(0), "why": why, "context": context})
    return found
