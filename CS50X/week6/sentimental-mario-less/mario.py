# TODO
from cs50 import get_int


def main():
    height = 0
    while height not in range(1, 9):
        height = get_int("Height: ")

    for j in range(1, height + 1):
        print(" " * (height - j) + "#" * j)


if __name__ == "__main__":
    main()
