class Month:
    def __init__(self, month_number):
        if 1 <= month_number <= 12:
            self.month_number = month_number
        else:
            raise ValueError("Номер месяца должен быть от 1 до 12")

    def get_month_number(self):
        return self.month_number

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.month_number - 1]

    def get_last_day_of_month(self):
        if self.month_number in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif self.month_number in {4, 6, 9, 11}:
            return 30
        else:
            return 29 if self.is_leap_year() else 28

    def get_first_day_of_month(self):
        days_in_month = {1: 31, 2: self.get_last_day_of_month(), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day_of_week = 0
        for month in range(1, self.month_number):
            day_of_week = (day_of_week + days_in_month[month]) % 7
        return day_of_week

    def get_last_day_of_month_weekday(self):
        first_day = self.get_first_day_of_month()
        last_day = (first_day + self.get_last_day_of_month() - 1) % 7
        return last_day

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)


month = Month(10)
print(f"Номер месяца: {month.get_month_number()}")
print(f"Название месяца: {month.get_month_name()}")
print(f"Номер последнего дня месяца: {month.get_last_day_of_month()}")
print(f"Номер дня недели первого дня месяца: {month.get_first_day_of_month()}")
print(f"Номер дня недели последнего дня месяца: {month.get_last_day_of_month_weekday()}")