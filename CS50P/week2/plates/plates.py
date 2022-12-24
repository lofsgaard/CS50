def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) <= 6 and len(s) >= 2 and s.isalnum():
        if s.isalpha():
            return True
        else:
            for c in s:
                if c.isalpha():
                    continue
                elif c.isdigit() and int(c) == 0:
                    break
                else:
                    return True

    else:
        return False





main()