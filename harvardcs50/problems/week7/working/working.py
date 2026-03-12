import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1)
    m2 = int(m2)

    if h1 > 12 or h2 > 12 or m1 > 59 or m2 > 59:
        raise ValueError

    start = convert_time(h1, m1, p1)
    end = convert_time(h2, m2, p2)

    return f"{start} to {end}"

def convert_time(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
