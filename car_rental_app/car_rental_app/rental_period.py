import datetime
class RentalPeriod:
    def __init__(self, start_date, start_time, end_date, end_time):
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time

    @staticmethod
    def validate_date(date_str):
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date < datetime.date.today():
                return False
            return date
        except ValueError:
            return False

    @staticmethod
    def validate_time(time_str):
        try:
            time = datetime.datetime.strptime(time_str, "%H:%M").time()
            if datetime.time(6, 0) <= time <= datetime.time(23, 0):
                return time
            return False
        except ValueError:
            return False

    def rental_days(self):
        return (self.end_date - self.start_date).days + 1

    def __str__(self):
        return f"Odbiór: {self.start_date} {self.start_time}, Zwrot: {self.end_date} {self.end_time}"

