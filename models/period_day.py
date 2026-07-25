import datetime

class PeriodDay:
    """
    Represents one day within a menstrual period.

    Stores daily information such as:
    - date of the period day
    - flow level
    - symptoms experienced
    - additional notes

    A period object can contain multiple PeriodDay objects to track changes throughout the menstrual cycle.
    """
    def __init__(self, date: datetime.date, flow=None, symptoms=None, note=""):
        self.date = date
        self.flow = flow
        self.symptoms = symptoms or []
        self.note = note