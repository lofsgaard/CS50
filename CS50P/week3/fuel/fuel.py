def main():
    x, y = get_fraction()
    calculate_fuel(x,y)

def get_fraction():
    while True:
        try:
            prompt = input("Fraction: ")
            x, y = prompt.split('/')
            if int(x) > int(y):
                raise ValueError
            else:
                return int(x), int(y)
        except ValueError:
            ...
        except ZeroDivisionError:
            ...

def calculate_fuel(x,y):
    result = x/y*100
    fuel = round(result)
    if fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{fuel}%")


main()