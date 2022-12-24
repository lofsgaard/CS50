# TODO
from cs50 import get_float
import math


def main():
    coins = get_input()
    calculate_change(coins)


def get_input():
    while True:
        try:
            coins = get_float("Change owed: ")
            if coins > 0:
                return coins
        except:
            return False


def calculate_change(n):
    coins = math.floor(n * 100)

    quarters = coins // 25
    dimes = (coins % 25) // 10
    nickels = ((coins % 25) % 10) // 5
    pennies = ((coins % 25) % 10) % 5

    owed = quarters + dimes + nickels + pennies

    print(f"{owed}")


if __name__ == "__main__":
    main()
