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

    def _update_date_range(self, new_date):
        """
        Updates the period's date range to include the given date.

        Intended for internal use when adding or modifying daily period records.
        """
        if self.start_date > new_date:
            self.start_date = new_date

        if self.end_date < new_date:
            self.end_date = new_date

    def _find_day_index(self, new_date):
        """
        Finds the index of a daily record with the given date.

        Returns None if no matching records exists.
        """
        for index, old_date in enumerate(self.days):
            if old_date.date == new_date:
                return index
        return None

    def add_day(self, day: PeriodDay):
        """
        Adds a daily record to the period.

        Updates the period's date range if necessary and keeps daily records sorted chronologically.
        """
        self._update_date_range(day.date)
        self.days.append(day)
        self.days.sort(key=lambda x: x.date)

    def update_day(self, new_day: PeriodDay):
        """
        Updates a daily record for the given date.

        Replaces an existing record with the same date.
        Adds a new record if no matching date exists.
        """
        index = self._find_day_index(new_day.date)
        if index is not None:
            self.days[index] = new_day
            return
        self.add_day(new_day)



