# here i will try to get input and check for the first capital letter then i will add _ to it and turn that capital letter into small

def main():
    camel = input("Please enter your string: ")
    print("snake_case: ", convert(camel))

def convert(camel):

    snake = ""

    for c in camel:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    return snake

if __name__ == "__main__":
    main()
