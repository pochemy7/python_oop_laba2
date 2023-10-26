import datetime


class Zate:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_day_of_week(self):
        return self.date.weekday()

    def get_day_name(self):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return days[self.get_day_of_week() ]

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.get_month() - 1]


zate = Zate(2023, 10, 1)

print(f"Год: {zate.get_year()}")
print(f"Месяц: {zate.get_month()}")
print(f"День: {zate.get_day()}")
print(f"Номер дня недели: {zate.get_day_of_week() + 1}")
print(f"Название дня недели: {zate.get_day_name()}")
print(f"Название месяца: {zate.get_month_name()}")