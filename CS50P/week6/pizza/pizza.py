import sys
from tabulate import tabulate
import csv

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3:
        sys.exit("To many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            open_file(sys.argv[1])
        else:
            sys.exit("Not a CSV file")


def open_file(name):
    try:
        with open(name) as f:
            reader = csv.reader(f, delimiter=',')
            header = []
            for row in reader:
                header.append(row)
            print(tabulate(header[1:], header[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()