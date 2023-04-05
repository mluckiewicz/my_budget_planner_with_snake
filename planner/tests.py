import datetime
from django.test import TestCase
from unittest import skip
from .utils.date_generator import DateCalculator
# Create your tests here.

class TestDateCalculator(TestCase):
    def setUp(self):
        self.start_date = datetime.date(2022, 1, 1)
        self.end_date = datetime.date(2022, 3, 31)
        self.dc = DateCalculator(self.start_date, self.end_date)

    def test_generate_daily_dates(self):
        dates = self.dc._generate_daily_dates()
        self.assertEqual(len(dates), (self.end_date - self.start_date).days + 1)

    def test_generate_weekly_dates(self):
        recurrence_value = 0 # Monday
        dates = self.dc._generate_weekly_dates(recurrence_value)
        for date in dates:
            self.assertEqual(date.weekday(), recurrence_value)

    def test_generate_monthly_dates(self):
        recurrence_value = 15 # 15th day of the month
        dates = self.dc._generate_monthly_dates(recurrence_value)
        self.assertEqual(len(dates), 3) # should generate 3 dates
        self.assertEqual(dates[0], self.start_date.replace(day=recurrence_value)) # first date should be the start date with the day replaced by the recurrence value
        for i in range(1, len(dates)):
            self.assertEqual(dates[i].day, recurrence_value) # all other dates should have the recurrence value as the day
               
    def test_generate_monthly_dates_next_year(self):
        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2023, 1, 31)
        target = [
            datetime.date(2022, 1, 15),
            datetime.date(2022, 2, 15),
            datetime.date(2022, 3, 15),
            datetime.date(2022, 4, 15),
            datetime.date(2022, 5, 15),
            datetime.date(2022, 6, 15),
            datetime.date(2022, 7, 15),
            datetime.date(2022, 8, 15),
            datetime.date(2022, 9, 15),
            datetime.date(2022, 10, 15),
            datetime.date(2022, 11, 15),
            datetime.date(2022, 12, 15),
            datetime.date(2023, 1, 15),
        ]
        dc = DateCalculator(start_date, end_date)
        recurrence_value = 15 # 15th day of the month
        dates = dc._generate_monthly_dates(recurrence_value)
        self.assertEqual(len(dates), 13) # should generate 3 dates
        self.assertEqual(dates[0], start_date.replace(day=recurrence_value)) # first date should be the start date with the day replaced by the recurrence value
        for i in range(1, len(dates)):
            self.assertEqual(dates[i], target[i]) # all other dates should have the recurrence value as the day

    def test_generate_quaterly_dates(self):
        # TODO add test for quarterly dates
        pass

    def test_get_dates_daily(self):
        dates = self.dc.get_dates('daily')
        self.assertEqual(len(dates), (self.end_date - self.start_date).days + 1)

    def test_get_dates_weekly(self):
        recurrence_value = 0 # Monday
        dates = self.dc.get_dates('weekly', recurrence_value)
        for date in dates:
            self.assertEqual(date.weekday(), recurrence_value)

    def test_get_dates_monthly(self):
        recurrence_value = 15 # 15th day of the month
        dates = self.dc.get_dates('monthly', recurrence_value)
        self.assertEqual(len(dates), 3) # should generate 3 dates
        self.assertEqual(dates[0], self.start_date.replace(day=recurrence_value)) # first date should be the start date with the day replaced by the recurrence value
        for i in range(1, len(dates)):
            self.assertEqual(dates[i].day, recurrence_value) # all other dates should have the recurrence value as the day

    def test_get_dates_quaterly(self):
        # TODO add test for quarterly dates
        pass