def main():
    get_input()


def get_input():
    shopping_list = {}
    while True:
        try:
            item = input().upper()
            key = item
            if item in shopping_list:
                shopping_list[key] += 1
            else:
                shopping_list[key] = 1
        except EOFError:
            final_list = dict(sorted(shopping_list.items(), key=lambda x: x[0]))
            for k, v in final_list.items():
                print(v, k)
            return False





main()