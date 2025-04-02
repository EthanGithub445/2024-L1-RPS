# Check that users have entered a valid
# option based on a list
import random


def string_checker(question, valid_ans=("yes", "no")):

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instruction():
    print('''
    instructions:

    ''')


def int_check(question):

    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # if integer is 1 or less print error message
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)
def rps_compare(user, comp):

    # If the user and the computer choice is the same, its a tie
    if user == comp:
        result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "paper":
        result = "win"

    # if its not a win or tie then its a lose
    else:
        result = "lose"

# main routine starts here

# initialize game variables


mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("Rock Paper Scissors game")
print()
# instructions
want_instructions = string_checker("do you want to read the instructions? ")

# check if yes or no
if want_instructions == "yes":
    instruction()

# ask for number of rounds / infinite mode
num_rounds = int_check("how many rounds would you like? push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # round headings
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (infinite mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"
    
    print(rounds_heading)

    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose ", user_choice)

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1
    print("rounds played: ", rounds_played)

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)
# game loop ends here

# game history / statistics area
