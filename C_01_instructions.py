# Check that users have entered a valid
# option based on a list
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


# Main routine
print()
print("Rock Paper Scissors")
print()

want_instructions = string_checker("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

print("program continues")
