def main():
    variable = input("camelCase: ")
    print("snake_case: ", end="")
    for c in variable:
        if c.islower():
            print(c, end="")
        if c.isupper():
            print("_", end="")
            print(c.lower(), end="")
    print()



main()