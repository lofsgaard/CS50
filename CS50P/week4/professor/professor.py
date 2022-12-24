import random


def main():
    x, y = generate_integer(get_level())
    count = 0
    score = 0
    while True:
        for i in range(len(x)):
            try:
                if count != 3 and score < 10:
                    z = x[i] + y[i]
                    answer = input(f'{x[i]} + {y[i]} = ')
                    if int(answer) == int(z):
                        score += 1
                    elif int(answer) != int(z) and count == 3:
                        print(z)
                    else:
                        raise ValueError
                elif score == 10:
                    print(f'Score {score}')
                    return False
            except ValueError:
                print('EEE')
                count += 1

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level <=3:
                return level
            else:
                continue
        except:
            ...


def generate_integer(n):

    if n == 1:
        x = random.sample(range(0, 10), 10)
        y = random.sample(range(0, 10), 10)
    elif n == 2:
        x = random.sample(range(10, 99), 10)
        y = random.sample(range(10, 99), 10)
    elif n == 3:
        x = random.sample(range(100, 999), 10)
        y = random.sample(range(100, 999), 10)
    print(x, y)
    return x, y



if __name__ == "__main__":
    main()