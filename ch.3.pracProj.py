def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def user_input_redux():
    print("please input a number")
    user_input = int(input())
    while user_input != 1:
        if user_input == 1:
            break
        user_input = collatz(user_input)
        print(user_input)
user_input_redux()