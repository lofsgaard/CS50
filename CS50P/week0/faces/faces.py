
def main():
    string = input()
    convert(string)

def convert(emoji):
    emoji = emoji.replace(":)", "🙂").replace(":(", "🙁")
    print(emoji)

main()