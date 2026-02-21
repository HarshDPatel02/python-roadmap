User = input ("What is the Answer to the Great Question of life, the universe, and everything? ")
User = User.strip().lower()

if User  == "42" or User == "forty-two" or User == "forty two":
    print("Yes")
else:
    print("No")
