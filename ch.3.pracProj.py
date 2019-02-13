def collatz(number):
    if number % 2 == 0:
        return print(number)
    else:
        return print(3 * number +1)

collatz(2)

def user_input_redux():
    print("please input a number")
    user_input = input()

    while user_input != 1:
        try:
            user_input = collatz(int(user_input))
        except:
            print("something went wrong")
            break
user_input_redux()