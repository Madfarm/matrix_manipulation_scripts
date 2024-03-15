from datetime import datetime, timedelta

def day_of_week(days):
    today = datetime.today()
    past_day = today - timedelta(days=days)
    return past_day.strftime('%A')

print(day_of_week(7))