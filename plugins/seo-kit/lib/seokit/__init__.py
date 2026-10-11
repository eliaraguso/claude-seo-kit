"""seo-kit shared library for the plugin's command-line scripts.

Standard library only; runs on CPython 3.9 and newer.
"""
import sys

__version__ = "1.0.0"
MIN_PYTHON = (3, 9)

if sys.version_info[:2] < MIN_PYTHON:  # pragma: no cover - exercised only on old interpreters
    sys.stderr.write(
        "seo-kit scripts need Python 3.9 or newer (found %d.%d)\n" % tuple(sys.version_info[:2])
    )
    sys.exit(2)
