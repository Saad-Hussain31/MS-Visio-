import datetime

current_date = datetime.datetime.now()


class date():
    def __init__(self, current_date):
        self.current_date = current_date

    def NumberOfDaysInMonth(self):
        daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.current_date.month == 2:
            if self.is_leap_year():
                return 29
            return daysOfMonths[self.current_date.month]
        else:
            return daysOfMonths[self.current_date.month]

    def is_leap_year(self):
        leap = False
        year = self.current_date.year
        if year % 400 == 0:
            leap = True
        else:
            if year % 4 == 0:
                if year % 100 != 0:
                    leap = True
        return leap

    def addDays(self, no_of_days):
        return (current_date + datetime.timedelta(no_of_days)).date()

    def subtractDays(self, no_of_days):
        return (current_date - datetime.timedelta(no_of_days)).date()


mydate = date(current_date)
print(mydate.is_leap_year())
print(mydate.NumberOfDaysInMonth())
print(mydate.addDays(5))
print(mydate.subtractDays(5))
