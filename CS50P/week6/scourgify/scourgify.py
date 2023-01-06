import sys
from tabulate import tabulate
import csv

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 4:
        sys.exit("To many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            change_file(open_file(sys.argv[1]), sys.argv[2])
        else:
            sys.exit("Not a CSV file")



def open_file(file):
    students = []
    try:
        with open(file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
    return students

def change_file(input, output):
    with open(output, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for student in input:
            lastname, firstname = student["name"].split(", ")
            house = student["house"]
            writer.writerow({"first": firstname, "last": lastname, "house": house})



if __name__ == "__main__":
    main()
