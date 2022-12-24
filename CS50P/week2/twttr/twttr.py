def main():
    string = input("Input: ")
    table = str.maketrans(dict.fromkeys('aeiouAEIOU'))
    print(string.translate(table))





main()