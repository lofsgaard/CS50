def main():
    prompt = input("What is the Answer to the Great Question of Life, the Universem and everything? ")
    if prompt.strip() == "42" or prompt.lower() == "forty two" or prompt.lower() == "forty-two":
        print("Yes")
    else:
        print("No")

main()