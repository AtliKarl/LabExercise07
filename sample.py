def main():
    user_input = input(print("Enter number: "))
    if both(user_input):
        print("FizzBuzz")
    elif divby5(user_input):
        print("Buzz")
    elif divby3(user_input):
        print("Fizz")
    else:
        print(str(user_input))