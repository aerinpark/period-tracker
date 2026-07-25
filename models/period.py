import datetime
from period_day import PeriodDay

class Period:
    """
    Represents one menstrual bleeding episode.

    Stores:
    - start and end dates of the bleeding episode
    - daily records containing flow, symptoms, and additional notes

    """
    def __init__(self, start_date: datetime.date, end_date: datetime.date,):
        if end_date and end_date < start_date:
            raise ValueError("End date cannot be earlier than start date")

        self.start_date = start_date
        self.end_date = end_date
        self.days = []

    def duration(self):
        """
        Returns the duration of the period in days.

        The duration is inclusive of both the start and end dates.
        Returns None if the period has ot ended.
        """
        return (self.end_date - self.start_date).days + 1

    def _update_date_range(self, new_date: datetime):
        """
        Updates the period's date range to include the given date.

        Intended for internal use when adding or modifying daily period records.
        """
        if self.start_date > new_date.date:
            self.start_date = new_date.date

        if self.end_date < new_date.date:
            self.end_date = new_date.date

    def add_day(self, day: PeriodDay):
        """
        Adds a daily record to the period cycle.

        Updates the period's date range if necessary.
        """
        self._update_date_range(day.date)
        self.days.append(day)




