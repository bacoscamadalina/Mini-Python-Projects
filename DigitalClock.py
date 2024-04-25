'''
                                  - DIGITAL CLOCK -
Create an application that displays the current time in the format of a digital clock in text mode, using the
characters _ and | as follows:
The current time will be displayed every 1 second. Values less than 10 will be preceded by a 0.
Pay attention to the time zone; it may be necessary to add a certain value to obtain the time in Romania.
The character 'o' will be used as separators between values.

Each digit in the display should occupy 4 characters, and the separators - 3 characters.
'''

import time

numbers = {
    '0': [' _ ', '| |', '|_|'],
    '1': ['   ', '  |', '  |'],
    '2': [' _ ', ' _|', '|_ '],
    '3': [' _ ', ' _|', ' _|'],
    '4': ['   ', '|_|', '  |'],
    '5': [' _ ', '|_ ', ' _|'],
    '6': [' _ ', '|_ ', '|_|'],
    '7': [' _ ', '  |', '  |'],
    '8': [' _ ', '|_|', '|_|'],
    '9': [' _ ', '|_|', ' _|'],
}
separator = ['   ', '   ', '   ']


def display_clock():
    while True:
        current_time = time.localtime()
        hour, minute, second = current_time.tm_hour, current_time.tm_min, current_time.tm_sec
        time_str = f'{hour:02d}o{minute:02d}o{second:02d}'

        for i in range(3):
            line = ''
            for digit in time_str:
                if digit == 'o':
                    line += separator[i]
                else:
                    line += numbers[digit][i]
            print(line)
        time.sleep(1)


display_clock()
