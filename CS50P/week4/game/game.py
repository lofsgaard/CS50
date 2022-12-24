import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if int(level) > 0:
                guess = int(input("Guess: "))
                rand = random.randint(0, int(level))
                if int(guess) > 0:
                    if int(guess) == int(rand):
                        print("Just right!")
                        break
                    elif int(guess) > int(rand):
                        print("Too large!")
                        continue
                    elif int(guess) < int(rand):
                        print("Too small!")
                        continue
                else:
                    continue
            else:
                continue
        except:
            continue






if __name__ == "__main__":
    main()