from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birth = input("Date of Birth:")
    minutes = minutes_since_birth(birth)
    words = number_to_words(minutes)
    print(f"{words} minutes".capitalize())

def minutes_since_birth(birth):
    try:
        year, month, day = birth.split("-")
        birth_date = date(int(year), int (month), int (day))

    except:
        sys.exit("Invalid date")

    today = date.today()

    if birth_date > today:
        sys.exit("Invalid date")

    delta = today - birth_date
    minutes = delta.days * 24 * 60
    return minutes

def number_to_words(num):
    words = p.number_to_words(num, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()
