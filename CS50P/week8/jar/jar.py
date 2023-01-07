class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._cookies = 0
        self._capacity = capacity

    def __str__(self):
        return '🍪' * self._cookies

    def deposit(self, n):
        if n > self._capacity - self._cookies:
            raise ValueError
        self._cookies = self._cookies + n

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError
        self._cookies = self._cookies - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies



def main():
    jar = Jar()
    jar.deposit(12)
    print(jar)





if __name__ == "__main__":
    main()