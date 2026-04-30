__all__ = [
	"DateInfo",
	"get_datetime",
	"capture_run_datetime",
	"get_run_datetime",
	"reset_run_datetime",
	"get_current_readable",
]

from dataclasses import dataclass
import datetime as date
from typing import Final


# In[ ]: Date formatting
# -----------------------------------------------------------------------
# NOTE: avoid expensive or stateful work at import time. Provide a small
# dataclass and a factory function so consumers (especially in notebooks)
# can call `get_datetime()` to get the current values when needed.


@dataclass(frozen=True)
class DateInfo:
	"""Immutable container with common formatted datetime strings.

	Fields:
	- now: timezone-naive datetime from datetime.now()
	- full_readable: e.g. 'Wednesday, Dec 24, 2025 at 03:12:45 PM'
	- readable: e.g. 'Dec 24, 2025 at 03:12 PM'
	- machine: ISO-like timestamp without colon in tz (to match previous)
	- iso: result of strftime using machine format
	- file_date: short date string 'YYYY-MM-DD'
	"""

	now: date.datetime
	full_readable: str
	readable: str
	machine: str
	iso: str
	file_date: str


def get_datetime(now: date.datetime | None = None) -> DateInfo:
	"""Return a DateInfo object with common formatted datetime strings.

	Parameters
	- now: optional datetime to format (defaults to datetime.now())

	This keeps import-time cheap and makes the API explicit for notebook use:
	>>> from faxlab_tools.utils.datetime import get_datetime
	>>> di = get_datetime()
	>>> di.file_date
	'2025-12-24'
	"""

	if now is None:
		now = date.datetime.now()

	date_full_readable_format: Final = "%A, %b %d, %Y at %I:%M:%S %p"
	date_readable_format: Final = "%b %d, %Y at %I:%M %p"

	# RFC3339 / ISO8601 compatible output with seconds precision.
	# If the datetime is naive, treat it as UTC for deterministic output.
	if now.tzinfo is None:
		now = now.replace(tzinfo=date.timezone.utc)

	# isoformat gives offsets with a colon (e.g. +05:30). For UTC, prefer 'Z'.
	iso = now.isoformat(timespec="seconds")
	if iso.endswith("+00:00"):
		iso = iso[:-6] + "Z"

	file_date = now.astimezone(date.timezone.utc).strftime("%Y-%m-%d")

	return DateInfo(
		now=now,
		full_readable=now.strftime(date_full_readable_format),
		readable=now.strftime(date_readable_format),
		machine="RFC3339(seconds)",
		iso=iso,
		file_date=file_date,
	)


# ------------------------------------------------------------------
# Run-pinning API
#
# For long-running notebooks/pipelines we want one immutable timestamp
#
_RUN_DATETIME: date.datetime | None = None


def capture_run_datetime(now: date.datetime | None = None) -> DateInfo:
	"""Capture and return a pinned DateInfo for the current run.

	If already captured, returns the existing pinned DateInfo. This lets
	notebooks capture a single timestamp at the start of a long run and
	reuse it for file names or burned-in image text.
	"""

	global _RUN_DATETIME
	if _RUN_DATETIME is None:
		_RUN_DATETIME = now or date.datetime.now()
	return get_datetime(_RUN_DATETIME)


def get_run_datetime() -> DateInfo | None:
	"""Return the pinned DateInfo if captured, else None."""

	if _RUN_DATETIME is None:
		return None
	return get_datetime(_RUN_DATETIME)


def reset_run_datetime() -> None:
	"""Reset the pinned run datetime (useful for tests)."""

	global _RUN_DATETIME
	_RUN_DATETIME = None


def get_current_readable() -> str:
	"""Return a human readable string for the current time.

	This differs from the pinned run datetime: it's intended as a quick
	helper to show the current time when needed (for logs, annotation,
	etc).
	"""

	return get_datetime().readable
