import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^([0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]) (AM|PM) to ([0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]) (AM|PM)$', s, re.IGNORECASE):
        '''
        matches.group(1) = hour 1
        matches.group(2) = minute 1
        matches.group(3) = AM or PM
        matches.group(4) = hour 2
        matches.group(5) = minute 2
        matches.group(6) = AM or PM
        '''
        if matches.group(3) == 'AM':
            if int(matches.group(1)) == 12:
                hour_start = 00
                minute_start = int(matches.group(2))
            else:
                hour_start = int(matches.group(1))
                minute_start = int(matches.group(2))
        elif matches.group(3) == 'PM':
            if int(matches.group(1)) == 12:
                hour_start = 00
                minute_start = int(matches.group(2))
            else:
                hour_start = int(matches.group(1)) + 12
                minute_start = int(matches.group(2))

        if matches.group(6) == 'AM':
            hour_end = int(matches.group(4))
            minute_end = int(matches.group(5))
        elif matches.group(6) == 'PM':
            if int(matches.group(4)) == 12:
                hour_end = int(matches.group(4))
                minute_end = int(matches.group(5))
            else:
                hour_end = int(matches.group(4)) + 12
                minute_end = int(matches.group(5))

        return f"{hour_start:02}:{minute_start:02} to {hour_end:02}:{minute_end:02}"

    elif matches := re.search(r'^([0-9]|1[0-2]) (AM|PM) to ([0-9]|1[0-2]) (AM|PM)$', s, re.IGNORECASE):
        '''
        matches.group(1) = hour 1
        matches.group(2) = AM or PM
        matches.group(3) = hour 2
        matches.group(4) = AM or PM

        '''
        if matches.group(2) == 'AM':
            if int(matches.group(1)) == 12:
                hour_start = 00
            else:
                hour_start = int(matches.group(1))
        elif matches.group(2) == 'PM':
            if int(matches.group(1)) == 12:
                hour_start = int(matches.group(1))
            else:
                hour_start = int(matches.group(1)) + 12

        if matches.group(4) == 'AM':
            if int(matches.group(3)) == 12:
                hour_end = 00
            else:
                hour_end = int(matches.group(3))
        elif matches.group(4) == 'PM':
            if int(matches.group(1)) == 12:
                hour_end = int(matches.group(3))
            else:
                hour_end = int(matches.group(3)) + 12
        return f"{hour_start:02}:00 to {hour_end:02}:00"
        
    else:
        raise ValueError


if __name__ == "__main__":
    main()
