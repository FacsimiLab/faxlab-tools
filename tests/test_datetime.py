import datetime as dt

from faxlab_tools.utils import datetime as fdt


def test_capture_and_get_run_datetime_pin():
    fdt.reset_run_datetime()
    fixed = dt.datetime(2020, 1, 2, 3, 4, 5)
    di1 = fdt.capture_run_datetime(now=fixed)
    di2 = fdt.get_run_datetime()
    assert di2 is not None
    assert di1.file_date == "2020-01-02"
    assert di2.file_date == "2020-01-02"


def test_capture_idempotent():
    fdt.reset_run_datetime()
    a = fdt.capture_run_datetime(now=dt.datetime(2021, 2, 3, 4, 5))
    b = fdt.capture_run_datetime(now=dt.datetime(1999, 1, 1))
    # second capture should not override first
    assert a.file_date == b.file_date


def test_get_current_readable_changes():
    # get_current_readable should return a string and reflect current time
    s1 = fdt.get_current_readable()
    s2 = fdt.get_current_readable()
    assert isinstance(s1, str)
    assert isinstance(s2, str)


def test_rfc3339_utc_and_offset():
    fdt.reset_run_datetime()
    # naive datetime should be treated as UTC per new policy
    naive = dt.datetime(2022, 1, 2, 3, 4, 5)
    di = fdt.get_datetime(now=naive)
    assert di.iso.endswith("Z")

    # tz-aware non-UTC
    import zoneinfo

    tz = zoneinfo.ZoneInfo("Asia/Kolkata")
    aware = dt.datetime(2022, 1, 2, 8, 34, 5, tzinfo=tz)
    di2 = fdt.get_datetime(now=aware)
    # offset for Asia/Kolkata is +05:30
    assert di2.iso.endswith("+05:30")
