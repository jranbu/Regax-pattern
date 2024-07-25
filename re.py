import re


text = '[["orders":[{"id"],["id"],["id":3},{"id":4},{"id"},{"id":6],["id"],["id":8},{"id":9},{"id":10), ("id":11},{"id":648},{"id":649),{"id":650},{"id":651),{"id":652), ("id":653)],"errors":[{"code" 3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)")))'


pattern = r'(?<="id":)\d+'
matches = re.findall(pattern, text)


ORANGE_BACKGROUND = '\033[48;5;214m'
RESET_COLOR = '\033[0m'


def format_with_orange_background(number):
    return f"{ORANGE_BACKGROUND}{number}{RESET_COLOR}"


formatted_numbers = [format_with_orange_background(num) for num in matches]


print("Numbers with orange background:")
for num in formatted_numbers:
    print(num)
