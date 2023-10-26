from datetime import datetime


class Period:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_seconds_difference(self):
        difference = (self.end_time - self.start_time).total_seconds()
        return int(difference)

    def get_minutes_difference(self):
        return self.get_seconds_difference() // 60

    def get_hours_difference(self):
        return self.get_minutes_difference() // 60

    def get_days_difference(self):
        return self.get_hours_difference() // 24

start_time = datetime(2023, 1, 3, 10, 25, 0)
end_time = datetime(2023, 1, 3, 14, 30, 0)

period = Period(start_time, end_time)

print(f"Разница в секундах: {period.get_seconds_difference()} секунд")
print(f"Разница в минутах: {period.get_minutes_difference()} минут")
print(f"Разница в часах: {period.get_hours_difference()} часов")
print(f"Разница в днях: {period.get_days_difference()} дней")