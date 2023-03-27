from __future__ import annotations
import datetime
from dateutil.relativedelta import relativedelta
import calendar


class DateCalculator:
    def __init__(self, start_date: datetime.date, end_date: datetime.date) -> None:
        """
        Constructs a new instance of the DateCalculator class.

        :param start_date: A datetime.date object representing the start date of the date range.
        :param end_date: A datetime.date object representing the end date of the date range.
        """
        self.start_date = start_date
        self.end_date = end_date

    def _generate_dates_in_daily_intervals(self) -> list[datetime.date]:
        """
        Generates a list of dates in daily intervals between the start date and the end date.

        :return: A list of datetime.date objects representing the dates in daily intervals.
        """
        dates = [
            date
            for date in (
                self.start_date + datetime.timedelta(i)
                for i in range((self.end_date - self.start_date).days + 1)
            )
        ]
        return dates

    def _generate_dates_in_weekly_intervals(
        self, recurrence_value: int
    ) -> list[datetime.date]:
        """
        Generates a list of dates in weekly intervals between the start date and the end date.

        :param recurrence_value: An integer representing the day of the week (0-6) on which to generate dates.
        :return: A list of datetime.date objects representing the dates in weekly intervals.
        """
        dates = [
            date
            for date in (
                self.start_date + datetime.timedelta(i)
                for i in range((self.end_date - self.start_date).days + 1)
            )
            if date.weekday() == recurrence_value
        ]
        return dates

    def _generate_dates_in_monthly_intervals(
        self, recurrence_value: int
    ) -> list[datetime.date]:
        """
        Generates a list of dates in monthly intervals between the start date and the end date.

        :param recurrence_value: An integer representing the day of the month (1-31) on which to generate dates.
        :return: A list of datetime.date objects representing the dates in monthly intervals.
        """
        dates = []
        months_in_period = (
            relativedelta(self.end_date, self.start_date).years * 12
            + relativedelta(self.end_date, self.start_date).months
        )
        dates.append(self.start_date + relativedelta(days=recurrence_value))

        for _ in range(months_in_period):
            next_date = dates[-1] + relativedelta(months=1, day=recurrence_value)
            dates.append(next_date)

        return dates

    def get_dates(
        self, unit: str, recurrence_value: int | None = None) -> list[datetime.date]:
        """
        Generates a list of dates between the start date and the end date, at intervals specified by the unit and recurrence value.

        :param unit: A string representing the interval unit. Valid options are "daily", "weekly", "monthly", "quaterly", and "annually".
        :param recurrence_value: An optional integer representing the interval recurrence value, depending on the unit. For "daily" and "weekly" intervals, this value is ignored. For "monthly" intervals, this value represents the day of the month (1-31) on which to generate dates.
        :return: A list of datetime.date objects representing the generated dates.
        """
        dates = []
        match unit.lower():
            case "daily":
                return self._generate_dates_in_daily_intervals()
            case "weekly":
                return self._generate_dates_in_weekly_intervals(recurrence_value)
            case "monthly":
                return self._generate_dates_in_monthly_intervals(recurrence_value)
            case "quaterly":
                # TODO 
                pass
            case "annually":
                # TODO 
                if calendar.isleap(current_date.year):
                    current_date += datetime.timedelta(days=366)
                else:
                    current_date += datetime.timedelta(days=365)
        return dates
