# Lucky Unicorn Fully Working Program v2
# Program should work - needs to be tested for usability

# Post Usability Testing Changes
# Added introduction rules at start of game
# Edited feedback messages to make it clear how much was being won and lost


import random

# Integer checking function below
def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)

# Main routine

# Introduction / Instructions

print("**** Welcome to the Lucky Unicorn Game ****")
print()
print("To play, enter an amount of money between $1 and $10 (whole dollars only).")
print()
print("- It costs $1/round")
print()
print("Payouts...")
print("- Unicorn: $5.00")
print("- Horse / Zebra: $0.50")
print("- Donkey: $0.00")
print()

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with? $", 1, 10)

print("***** Game in Progress ******")

keep_going = ""
while keep_going == "":

    # tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    print()
    print("------------------")
    print("It's a {}".format(token))
    print("------------------")

    # Adjust balance based on the chosen token and generate feedback
    if token == "unicorn":
        balance += 5    # wins $5
        feedback = "Congratulations! You won $5.00"
    elif token == "donkey":
        balance -= 1    # does not win anything (ie: loses $1)
        feedback = "Sorry, you did not win anything this round"
    else:
        balance -= 0.5  # 'wins' 50c, paid $1 so loses 50c
        feedback = "Good try. You won back 50c"

    print()
    print(feedback)
    print("Balance: ${:.2f}".format(balance))
    print()

    # If user has enough money to play, ask if they want to play again...
    if balance < 1:
        print("Sorry you don't have enough money to continue.  Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

# farewell user at end of game.
print("Thank you for playing.  You leave the game with ${:.2f}".format(balance))
