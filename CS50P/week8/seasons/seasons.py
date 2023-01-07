from datetime import date, datetime
import re
import inflect
import sys

p = inflect.engine()

def main():
    print(convert_date(input('Date of Birth: ')) + ' minutes')


def convert_date(birth):
    if not re.search(r"\d{4}-\d{2}-\d{2}", birth):
       sys.exit("Invalid date")
    todays_date = date.today()
    date_object_today = datetime.strptime(str(todays_date), '%Y-%m-%d').date()
    date_object_birth = datetime.strptime(birth, '%Y-%m-%d').date()
    age = date_object_today - date_object_birth
    words = p.number_to_words(age.days * 24 * 60, andword="")
    return words.capitalize()


if __name__ == "__main__":
    main()
