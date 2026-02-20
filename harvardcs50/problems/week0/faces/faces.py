def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    User_input = input("Please enter message here: ")
    msg = convert(User_input)
    print(msg)




main()
