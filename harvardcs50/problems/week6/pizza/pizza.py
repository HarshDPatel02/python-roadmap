import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit("too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a csv file")

    try:
        with open(filename) as file:
            reader = csv.reader(file)

            table = []
            headers = next(reader)

            for row in reader:
                table.append(row)

            print(tabulate(table, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
