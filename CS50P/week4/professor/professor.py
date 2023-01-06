import random
import sys


def main():
    level = get_level()
    fails = 1
    score = 0
    for i in range(10):
        x = generate_integer(level)
        for j in range(1):
            y = generate_integer(level)
            answer = x + y
            problem = input(f"{x} + {y} = ")

            if answer == int(problem):
                score += 1

            while answer != int(problem):
                fails += 1
                print("EEE")
                problem = input(f"{x} + {y} = ")
                if fails >= 3:
                    print(answer)
                    sys.exit("Score: " + str(score))
    print("Score: " + str(score))





def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level == 1:
                return level
            elif level == 2:
                return level
            elif level == 3:
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 10)
        return x
    elif level == 2:
        x = random.randint(10, 99)
        return x
    elif level == 3:
        x = random.randint(100, 999)
        return x


if __name__ == "__main__":
    main()
