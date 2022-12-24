def main():
    coins = 50
    while True:
        print("Amount Due: ", coins)
        insert = int(input("Insert coin: "))
        if insert == 5 or insert == 10 or insert == 25:
            coins = coins - insert
            if coins <= 0:
                print("Change owed: ", abs(coins))
                break
            continue
        else:
            continue


main()