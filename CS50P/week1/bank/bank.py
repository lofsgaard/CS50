def main():
    greeting = input("Greeting: ")
    if greeting.strip().lower().startswith('hello'):
        print("$0")
    elif greeting.lower().startswith('h') and greeting != "hello":
        print("$20")
    else:
        print("$100")


main()