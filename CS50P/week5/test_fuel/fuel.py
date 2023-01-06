def main():
    prompt = input("Fraction: ")
    print(gauge(convert(prompt)))


def convert(fraction):
    x, y = fraction.split('/')
    while True:
        try:
            if int(x) > int(y):
                raise ValueError('x is bigger than y')
            else:
                result = int(x)/int(y)*100
                fuel = round(result)
                return int(fuel)
        except ValueError:
            return ValueError
        except ZeroDivisionError:
            return ZeroDivisionError


def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()