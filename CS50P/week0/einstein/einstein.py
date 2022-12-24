def main():
    m = int(input("m: "))
    print(einstein(m))

def einstein(kg):
    E = kg * pow(300000000, 2)
    return E

main()