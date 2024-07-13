from .find_word import find_word

def validate_input(input):
    if find_word('week')(input) or find_word('days')(input) or find_word('day')(input) or find_word('hours')(input) or find_word('hour')(input):
        # Check for valid arguments for hours or days
        if 'hours' in input or 'days' in input:
            command_arr = input.split()
            if not command_arr[0].isdigit():
                return 'Enter a valid number'
            if not len(command_arr) == 2:
                return 'Too much entered'
        # Check for valid arguments for hour, day, or week
        elif 'hour' in input or 'day' in input or 'week' in input:
            command_arr = input.split()
            if not len(command_arr) == 1:
                if 'hour' in input:
                    return 'Enter "hour" or "_ hours"'
                elif 'day' in input:
                    return 'Enter "day" or "_ days"'
                else:
                    return 'Enter "week"'
    else:
        return 'Please enter the amount of time as specified: \n   > hour\n   > _ hours\n   > day\n   > _ days\n   > week'
    return 'Valid'
