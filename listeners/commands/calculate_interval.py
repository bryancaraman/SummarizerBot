import time
from .find_word import find_word

def calculate_interval(input):
    time = 0
    if find_word('hour')(input):
        # calc 1 hour
        pass
    elif find_word('day')(input):
        # calc 1 day
        pass
    elif find_word('week')(input):
        pass
    elif find_word('days')(input):
        pass
    else:
        pass
    return time
        