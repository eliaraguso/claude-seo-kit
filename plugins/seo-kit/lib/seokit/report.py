"""Output helpers: UTF-8 console setup and JSON serialisation."""
from __future__ import annotations

import dataclasses
import json
import sys


def setup_stdout() -> None:
    """Make stdout/stderr UTF-8 (Windows consoles default to a legacy code page).

    Call this before printing anything.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):  # replaced or detached streams
            pass


def _default(obj):
    if isinstance(obj, (set, frozenset)):
        return sorted(obj, key=str)
    if isinstance(obj, bytes):
        return obj.decode("utf-8", "replace")
    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        return dataclasses.asdict(obj)
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    return str(obj)


def dumps(obj, indent: int = 2) -> str:
    """JSON text with real UTF-8 characters (ensure_ascii=False)."""
    return json.dumps(obj, ensure_ascii=False, indent=indent, default=_default)


def print_json(obj) -> None:
    print(dumps(obj))


def write_json(path: str, obj) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(dumps(obj))
        fh.write("\n")


def eprint(*args) -> None:
    """Print to stderr."""
    print(*args, file=sys.stderr)
