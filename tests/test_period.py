import pytest
from datetime import date
from models.period import Period
from models.period_day import PeriodDay

def test_create_period():
    period = Period(
        start_date=date(2026, 7, 27),
        end_date=date(2026, 7,30)
    )

    assert period.start_date == date(2026, 7, 27)
    assert period.end_date == date(2026, 7, 30)
    assert period.days == []

def test_create_period_with_value_error():
    with pytest.raises(ValueError,
                       match="End date cannot be earlier than start date"
                       ):
        Period(
        start_date=date(2026,7,30),
        end_date=date(2026,7,27)
    )

def test_check_period_duration():
    period = Period(
        start_date=date(2026, 7, 27),
        end_date=date(2026, 7, 30)
    )
    assert period.duration() == 4

def test_add_period_day_and_update_duration():
    period = Period(
        start_date=date(2026, 7, 27),
        end_date=date(2026, 7, 28)
    )
    day = PeriodDay(
        date=date(2026, 7, 30),
        flow="light"
    )
    period.add_day(day)
    assert len(period.days) == 1
    assert period.days[0] == day
    assert period.end_date == date(2026, 7, 30)
    assert period.duration() == 4

def test_update_start_end_date():
    period = Period(
        start_date=date(2026, 7, 28),
        end_date=date(2026, 7, 29)
    )
    period.add_day(PeriodDay(
        date=date(2026, 7, 27),
    ))
    period.add_day(PeriodDay(
        date=date(2026, 7, 30),
    ))
    assert period.start_date == date(2026, 7, 27)
    assert period.end_date == date(2026, 7, 30)
    assert period.duration() == 4
