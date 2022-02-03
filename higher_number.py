'''
Game: user types in a number,
and the computer tries to think of a 
higher one.
'''

def higher_num(x):
    return x + 1

def get_user_number():
    n = input("Pick any number: ")
    return float(n)

def print_computer_number(n):
    print(f"The computer played: {n}")


def play_higher_number_game():
    rounds = int(input("How many rounds do you want to play? "))

    for i in range(rounds):
        user_number = get_user_number()
        computer_number = higher_num(user_number)
        print_computer_number(computer_number)
