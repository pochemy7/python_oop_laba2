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


zate = Zate(2023, 10, 26)

print(f"Год: {zate.get_year()}")
print(f"Месяц: {zate.get_month()}")
print(f"День: {zate.get_day()}")
print(f"Номер дня недели: {zate.get_day_of_week() + 1}")
print(f"Название дня недели: {zate.get_day_name()}")
print(f"Название месяца: {zate.get_month_name()}")

class ZateExt(Zate):
    def add_years(self, years):
        new_date = self.date.replace(year=self.get_year() + years)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def subtract_years(self, years):
        new_date = self.date.replace(year=self.get_year() - years)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def add_months(self, months):
        new_year = self.get_year() + (self.get_month() + months - 1) // 12
        new_month = (self.get_month() + months - 1) % 12 + 1
        new_day = min(self.get_day(), self.get_last_day_of_month(new_year, new_month))
        return ZateExt(new_year, new_month, new_day)

    def subtract_months(self, months):
        new_year = self.get_year() - (months - 1) // 12
        new_month = (self.get_month() - (months - 1)) % 12
        if new_month == 0:
            new_month = 12
        new_day = min(self.get_day(), self.get_last_day_of_month(new_year, new_month))
        return ZateExt(new_year, new_month, new_day)

    def add_days(self, days):
        new_date = self.date + datetime.timedelta(days=days)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def subtract_days(self, days):
        new_date = self.date - datetime.timedelta(days=days)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def get_last_day_of_month(self, year, month):
        if month == 12:
            return 31
        return (datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)).day


zate_ext = ZateExt(2023, 10, 24)

new_date1 = zate_ext.add_years(2)
new_date2 = zate_ext.subtract_years(1)

new_date3 = zate_ext.add_months(6)
new_date4 = zate_ext.subtract_months(3)

new_date5 = zate_ext.add_days(15)
new_date6 = zate_ext.subtract_days(7)

print(f"Текущая дата: {zate_ext.get_year()}-{zate_ext.get_month()}-{zate_ext.get_day()}")
print(f"Прибавляем 2 года: {new_date1.get_year()}-{new_date1.get_month()}-{new_date1.get_day()}")
print(f"Отнимаем 1 год: {new_date2.get_year()}-{new_date2.get_month()}-{new_date2.get_day()}")
print(f"Прибавляем 6 месяцев: {new_date3.get_year()}-{new_date3.get_month()}-{new_date3.get_day()}")
print(f"Отнимаем 3 месяца: {new_date4.get_year()}-{new_date4.get_month()}-{new_date4.get_day()}")
print(f"Прибавляем 15 дней: {new_date5.get_year()}-{new_date5.get_month()}-{new_date5.get_day()}")
print(f"Отнимаем 7 дней: {new_date6.get_year()}-{new_date6.get_month()}-{new_date6.get_day()}")
