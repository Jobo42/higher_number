'''
Game: user inputs a number and the computer
spits out a lower one.
'''

def lower_number(n):
    return n-1

def get_user_number():
    n = input("Pick any number: ")
    return float(n)

def print_computer_number(n):
    print(f"The computer played: {n}")

user_number = get_user_number()
computer_number = lower_number(user_number)
print_computer_number(computer_number)