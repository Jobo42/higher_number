'''
Game: user inputs a number and the computer
spits out a lower one.
'''

def lower_number(n):
    return n-1

def much_lower_number(n):
    return n - 100*n

def get_user_number():
    n = input("Pick any number: ")
    return float(n)

def get_game_difficulty():
    difficulty = input("What difficulty do you want to play, (h)ard or (e)asy? ")
    return difficulty

def print_computer_number(n):
    print(f"The computer played: {n}")
    print("I win!!!")

difficulty = get_game_difficulty()
user_number = get_user_number()

# Hard mode
if difficulty == "h":
    computer_number = much_lower_number(user_number)
# Easy mode
elif difficulty == "e":
    computer_number = lower_number(user_number)

print_computer_number(computer_number)