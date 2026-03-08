def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    print(gauge(percent))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError

        percentage = round((x / y) * 100)
        return percentage

    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
