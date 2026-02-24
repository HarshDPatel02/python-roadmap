# if u look closely in code vowel are skio so we have to find vowel in strong and remove them and print new string

def main():
    text = input("Please enter your string:")
    print("Output:", remove_vowels(text))

def remove_vowels(text):
    result = ""
    for c in text:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            result += c
    return result

if __name__ == "__main__":
    main()
