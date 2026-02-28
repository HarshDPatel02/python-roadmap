def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    while True:
        date_input = input("Date: ").strip()

        # Numeric format: MM/DD/YYYY
        if "/" in date_input:
            try:
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                    break
            except ValueError:
                continue

        # Textual month format: Month DD, YYYY (comma is required)
        else:
            if date_input.count(",") != 1:
                continue  # reject missing comma

            try:
                month_day, year = date_input.split(",")
                month_day = month_day.strip().split()
                if len(month_day) != 2:
                    continue

                month_str, day = month_day
                if month_str not in months:
                    continue

                month = months.index(month_str) + 1
                day = int(day)
                year = int(year.strip())

                if 1 <= day <= 31:
                    print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                    break
            except ValueError:
                continue


if __name__ == "__main__":
    main()
