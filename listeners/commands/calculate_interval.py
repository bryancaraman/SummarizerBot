import datetime
import time

def calculate_interval(time_input):
    if 'week' in time_input:
        beginning_of_today = datetime.date.today()
        time_since_monday = datetime.timedelta(days=beginning_of_today.weekday())
        return int(beginning_of_today.strftime("%s")) - time_since_monday.days * 86400
    elif 'days' in time_input:
        # Beginning of the day _ days back
        split_input = time_input.split()
        beginning_of_today = int(datetime.date.today().strftime("%s"))
        days_ago = int(split_input[0]) * 86400
        return beginning_of_today - days_ago
    elif 'day' in time_input:
        # Since the beginning of today
        return datetime.date.today().strftime("%s")
    elif 'hours' in time_input:
        split_input = time_input.split()
        return time.time() - int(split_input[0]) * 3600
    elif 'hour' in time_input:
        return time.time() - 3600
    else:
        return 'Input validation failed'
        