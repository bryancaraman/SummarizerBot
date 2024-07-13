import re

# Use regex in order to verify valid time input
def find_word(word):
    return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search