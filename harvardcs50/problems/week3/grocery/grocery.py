def main():
    items = {}

    while True:
        try:
            item_input = input().strip().upper()
            if item_input in items:
                items[item_input] += 1
            else:
                items[item_input] = 1
        except EOFError:
            break

    for item in sorted(items):
        print(items[item], item)


if __name__ == "__main__":
    main()
