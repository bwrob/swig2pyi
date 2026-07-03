import QuantLib as ql


def test_date() -> None:
    d = ql.Date(19, ql.May, 2026)
    assert d.dayOfMonth() == 19
    assert d.month() == ql.May
    assert d.year() == 2026


def test_calendar() -> None:
    cal = ql.TARGET()
    d = ql.Date(1, ql.January, 2026)
    assert not cal.isBusinessDay(d)
