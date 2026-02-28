"""
what we have to do in this
some what like fuel indicator , like 1/4 indicates tank is 25% full, 1/2 = 50%, 3/4 tnak is 75%
we have to take units from user in x/y fromat which is non negative and y is positive number, and the
output as percentage if 1 or less percentage then inticater "e" and will 99 or 100 then indicate "F"

"""

def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            x,y = fraction.split("/")

            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError

            if x > y or x < 0:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()

