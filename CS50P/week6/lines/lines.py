import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3:
        sys.exit("To many command-line arguments")
    else:
        if sys.argv[1].endswith(".py"):
            open_file(sys.argv[1])
        else:
            sys.exit("Not a python file")


def open_file(name):
    line_count = 0
    try:
        with open(name) as f:
            lines = f.readlines()
            for line in lines:
                line = line.lstrip(" ")
                if line == '\n' or line.lstrip().startswith('#'):
                    ...
                else:
                    line_count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(line_count)


if __name__ == "__main__":
    main()
