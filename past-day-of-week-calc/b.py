from datetime import datetime, timedelta

def days_prior_to_today(days):
    today = datetime.today()
    days_ago = today - timedelta(days=days)
    return days_ago.strftime('%A')

print(days_prior_to_today(5))  # Output: Saturda