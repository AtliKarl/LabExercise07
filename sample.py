def divby5(i):
    pass

def divby3(i):
    pass

def both(i):
    pass

def main():
    user_input = input("Enter a number: ")
    if both(user_input):
        print("FizzBuzz")
    elif divby5(user_input):
        print("Buzz")
    elif divby3(user_input):
        print("Fizz")
    else:
        print(str(user_input))
main()