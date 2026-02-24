"""
there are few rules to solve this
first one is:
* minimum 2 charater and max 6
* must start with two characters with letter
* only letter and numbers are allowed
* number must be at the end
* first number cant be zero
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):

     # length check
     if len(s) < 2 or len(s) > 6:
         return False
     # must start with at least two letters
     if not s[0].isalpha() or not s[1].isalpha():
         return False
     # only letters and number allowed
     if not s.isalnum():
         return False
     # NUmber must be at the end
     number_started = False

     for char in s:
         if char.isdigit():

             if not number_started and char =="0":
                 return False

             number_started = True

         else:
            if number_started:
                return False
     return True

if __name__ == "__main__":
 main()
