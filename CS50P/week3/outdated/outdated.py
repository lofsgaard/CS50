def main():
    get_input()

outdated = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def get_input():
    while True:
        try:
            user = input('Date: ').strip()
            if '/' in user:
                month, day, year = user.split('/')
                if int(month) <= 12 and int(day) <= 31:
                    print(f'{year}', end='')
                    print("-", end='')
                    print(f'{int(month):02}', end='')
                    print("-", end='')
                    print(f'{int(day):02}')
                    break

            if ',' in user:
                month, day, year = user.split(' ')
                day = day.rstrip(',')
                if month in outdated and int(day.rstrip(',')) <= 31:
                    month = int(outdated.index(month) + 1)
                    print(year, end='')
                    print("-", end='')
                    print(f'{int(month):02}', end='')
                    print("-", end='')
                    print(f'{int(day):02}')
                    break

        except ValueError:
            print('value error????')

main()