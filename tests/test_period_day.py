from datetime import date
from models.period_day import PeriodDay

def test_create_period_day():
    period_day = PeriodDay(
        date(2026,7,27),
        "medium",
        ["cramps", "nausea"],
        'first day'
    )
    assert period_day.date == date(2026,7,27)
    assert period_day.flow == "medium"
    assert period_day.symptoms == ["cramps", "nausea"]
    assert period_day.note == "first day"

def test_check_period_day_default_values():
    period_day = PeriodDay(
        date=date(2026,6,29)
    )
    assert period_day.date == date(2026,6,29)
    assert period_day.flow is None
    assert period_day.symptoms == []
    assert period_day.note == ""