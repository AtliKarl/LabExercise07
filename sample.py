def divby5(i):
    if int(i) % 5 == 0:
        return True
    else:
        return False


def divby3(i):
    if int(i) % 3 == 0:
        return True
    else:
        return False


def both(i):
    if divby3(i) and divby5(i):
        return True
    else:
        return False


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
