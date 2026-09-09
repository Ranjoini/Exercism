import calendar
from datetime import date


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.
    """

    def __init__(self, message):
        super().__init__(message)


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    # 1. The Translators
    weekday_map = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    index_map = {
        "first": 0,
        "second": 1,
        "third": 2,
        "fourth": 3,
        "fifth": 4,
        "last": -1,
    }

    target_weekday = weekday_map[day_of_week]

    # 2. Find the boundaries of the month
    _, num_days = calendar.monthrange(year, month)

    # 3. The Collector Loop
    matching_days = []
    for day in range(1, num_days + 1):
        current_date = date(year, month, day)
        if current_date.weekday() == target_weekday:
            matching_days.append(current_date)

    # 4. The "Teenth" Dispatcher
    if week == "teenth":
        for d in matching_days:
            if 13 <= d.day <= 19:
                return d

    # 5. The Standard Index Dispatcher with Error Handling
    try:
        target_index = index_map[week]
        return matching_days[target_index]
    except IndexError:
        raise MeetupDayException("That day does not exist.")
