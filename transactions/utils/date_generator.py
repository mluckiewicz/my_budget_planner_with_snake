from __future__ import annotations
import datetime
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
        self.dates = []

    def _generate_daily_dates(self) -> list[datetime.date]:
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

    def _generate_weekly_dates(self, recurrence_value: int) -> list[datetime.date]:
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

    def _generate_monthly_dates(
        self, recurrence_value: int | None = None
    ) -> list[datetime.date]:
        """
        Generates a list of dates in monthly intervals between the start date and the end date.

        :param recurrence_value: An integer representing the day of the month (1-31) on which to generate dates.
        :return: A list of datetime.date objects representing the dates in monthly intervals.
        """
        dates = []
        current_date = (
            self.start_date.replace(day=recurrence_value)
            if recurrence_value
            else self.start_date
        )

        while current_date <= self.end_date:
            dates.append(current_date)
            
            # Period is over 12 months
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
                
            else:
                if current_date.month + 1 == 2 and recurrence_value > 28:
                    current_date = current_date.replace(
                        month=current_date.month + 1, day=28
                    )

                elif recurrence_value == 31:
                    current_date = current_date.replace(
                        month=current_date.month + 1,
                        day=calendar.monthrange(
                            current_date.year, current_date.month + 1
                        )[1],
                    )
                else:
                    current_date = current_date.replace(month=current_date.month + 1)
        return dates

    #! NIE DZIAŁA ZGODNIE Z ZAŁOŻENIEM
    def _generate_quaterly_dates(self) -> list[datetime.date]:
        # TODO Need to write function to calculate quater duration
        days_per_qtr = {1: 91, 2: 91, 3: 92, 4: 92}

        duration = (self.end_date - self.start_date).days
        dates = list([self.start_date])
        current_quarter = (self.start_date.month - 1) // 3 + 1
        next_date = self.start_date + datetime.timedelta(
            days=days_per_qtr.get(current_quarter)
        )

        while next_date <= self.start_date + datetime.timedelta(days=duration):
            dates.append(next_date)
            next_quarter = (next_date.month - 1) // 3 + 1
            next_date += datetime.timedelta(days=days_per_qtr.get(next_quarter))
        return dates

    def _generate_annually_dates(self, recurrence_value: int) -> list[datetime.date]:
        pass

    def get_dates(
        self, unit: str, recurrence_value: int | None = None
    ) -> list[datetime.date]:
        """
        Generates a list of dates between the start date and the end date, at intervals specified by the unit and recurrence value.

        :param unit: A string representing the interval unit. Valid options are "daily", "weekly", "monthly", "quaterly", and "annually".
        :param recurrence_value: An optional integer representing the interval recurrence value, depending on the unit. For "daily" and "weekly" intervals, this value is ignored. For "monthly" intervals, this value represents the day of the month (1-31) on which to generate dates.
        :return: A list of datetime.date objects representing the generated dates.
        """
        match unit.lower():
            case "daily":
                return self._generate_daily_dates()
            case "weekly":
                return self._generate_weekly_dates(recurrence_value)
            case "monthly":
                return self._generate_monthly_dates(recurrence_value)
            case "quaterly":
                return self._generate_quaterly_dates()
