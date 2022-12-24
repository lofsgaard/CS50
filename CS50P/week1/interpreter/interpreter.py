def main():
    math = input("Expression: ")
    x, y ,z = math.split(" ")
    if y == "+":
        print(float(x)+float(z))
    elif y == "-":
        print(float(x)-float(z))
    elif y == "*":
        print(float(x)*float(z))
    elif y == "/":
        print(float(x)/float(z))

main()