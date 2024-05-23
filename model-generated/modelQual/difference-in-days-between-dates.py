from datetime import datetime

def days_between(d1, d2):
    return abs((d2 - d1).days)

print(f"It's been {days_between(datetime(2024, 4, 8), datetime(2024, 5, 22))} since the last episode of Invincible aired.")