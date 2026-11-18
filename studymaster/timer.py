class StudySession:

    def __init__(self):
        self.minutes = 0

    def add_time(self, minutes):
        self.minutes += minutes

    def total_hours(self):
        return round(self.minutes / 60, 2)
