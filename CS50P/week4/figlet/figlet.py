from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
random = random.choice(fonts)

def main():

    if len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font" :
        f = sys.argv[2]
        if f in fonts:
            s = input("Input: ")
            figlet.setFont(font=f)
            print(figlet.renderText(s))
        else:
            sys.exit("Invalid usage")

    elif len(sys.argv) == 1:
        s = input("Input: ")
        f = get_font()
        figlet.setFont(font=f)
        print(figlet.renderText(s))

    else:
        sys.exit("Invalid usage")


def get_font():
    font = figlet.setFont(font=random)
    return font




if __name__ == "__main__":
    main()