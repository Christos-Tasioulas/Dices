import random

def parse_input(input_string):
    
    return int(input_string)

"""
    Return `input_string` as an even integer between 4 and 12 or 20 or 100.

    Check if `input_string` is an even integer number between 4 and 12 or 20 or 100.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
"""
def parse_dice(input_string):
    if input_string.strip() in {"4", "6", "8", "10", "12", "20", "100"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def roll_dice(num_dice, n):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and n, inclusive.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, n)
        roll_results.append(roll)
    return roll_results

def roll_d4(num_dice):

    return roll_dice(num_dice, 4)

def roll_d6(num_dice):

    return roll_dice(num_dice, 6)

def roll_d8(num_dice):

    return roll_dice(num_dice, 8)

def roll_d10(num_dice):

    return roll_dice(num_dice, 10)

def roll_d_percentage(num_dice):

    results = roll_dice(num_dice, 10)
    for i in range(len(results)):
        results[i] = 10*results[i]
    
    return results

def roll_d12(num_dice):

    return roll_dice(num_dice, 12)

def roll_d20(num_dice):

    return roll_dice(num_dice, 20)

# ~~~ App's main code block ~~~

# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll?")
num_dice = parse_input(num_dice_input)

n_input = input("What dice do you want to roll?")
n = parse_dice(n_input)

# 2. Roll the dice
if(n == 100):
    dice = "roll_d_percentage"
else:
    dice = "roll_d" + str(n)

roll_results = eval(dice + "(" + str(num_dice) + ")")
print(roll_results)  # Remove this line after testing the app