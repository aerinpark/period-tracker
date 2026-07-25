import datetime

class Period:
    """
    Represents one menstrual bleeding episode.

    Stores:
    - start and end dates of the bleeding episode
    - daily records containing flow, symptoms, and additional notes

    """
    def __init__(self, start_date: datetime.date, end_date: datetime.date,):
        self.start_date = start_date
        self.end_date = end_date
        self.days = []

