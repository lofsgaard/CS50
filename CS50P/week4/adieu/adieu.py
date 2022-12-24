import inflect

p = inflect.engine()

def main():
    adieu(get_name())


def get_name():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            return names

def adieu(names):
    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()