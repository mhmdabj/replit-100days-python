import datetime

def print_date(year, month, day):
    myDate = datetime.date(year=year, month=month, day=day)
    print(myDate)
    return myDate

def print_date_plus_days(days):
    today = datetime.date.today()
    difference = datetime.timedelta(days=days)
    newDate = today + difference
    print(newDate)
    return newDate

def holiday_status(holiday_date):
    today = datetime.date.today()
    if holiday_date > today:
        print("Coming soon")
        return "Coming soon"
    elif holiday_date < today:
        print("Hope you enjoyed it")
        return "Hope you enjoyed it"
    else:
        print("HOLIDAY TIME!")
        return "HOLIDAY TIME!"

def event_countdown(day, month, year):
    today = datetime.date.today()
    event = datetime.date(year, month, day)
    difference = (event - today).days
    if difference > 0:
        print(f"{difference} days to go")
        return difference
    elif difference < 0:
        print(f"😭😭😭😭😭😭😭 You missed it by {abs(difference)} days!")
        return difference
    else:
        print("🥳🥳🥳🥳🥳🥳🥳 Today!")
        return 0

if __name__ == "__main__":
    print_date(2022, 12, 7)
    print_date_plus_days(14)
    holiday_status(datetime.date(2025, 9, 24))
    event_countdown(1, 1, 2100) 