import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        return False

    parts = ip.split(".")

    for part in parts:
        if part != "0" and part.startswith("0"):
            return False
        num = int(part)

        if num < 0 or num > 255:
            return False


    return True

if __name__ == "__main__":
    main()
