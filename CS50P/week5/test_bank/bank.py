def main():
    print(value(input("Greeting: ")))

def value(greeting):
    if greeting.strip().lower().startswith('hello'):
        return 0
    elif greeting.lower().startswith('h') and greeting != "hello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()