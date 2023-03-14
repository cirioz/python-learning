
#! Higher or Lower - Angela Solution

# We need to develop the skill of braking down problams.

from art import logo, vs
from game_data import data
import random

def format_data(account):
#! """ Format the account data into printable format."""
    account_name = account["name"]
    account_descrpt = account["description"]
    account_cntry = account["country"]
    # account_flwr_cnt = account["follower_count"]
    return f"{account_name}, a {account_descrpt}, from {account_cntry}"

## Use if statement to check if user is correct.
def check_answer(guess, a_flwr_cnt, b_flwr_cnt):
    """Take the user guesss and follower counts and returns if they got it right"""
    # if a_flwr_cnt > b_flwr_cnt:
    #     if guess == "a":
    #         return True
    #     else:
    #         return False
    if a_flwr_cnt > b_flwr_cnt:
        return guess == "a"
    else:
        return guess == "b"
        

#? Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    #? Random generated accounts
    account_a = account_b
    account_b = random.choice(data)
    
    #! if acc a == b, regenerate acc b
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")





    #? Pull a random account from the game data list



    #? Format the account data into printable format.
    account_name = account_a["name"]
    account_descrpt = account_a["description"]
    account_cntry = account_a["country"]

    # print(f"{account_name}, a {account_descrpt}, from {account_cntry}")

    #? Aks user for a guess.

    guess = input("Who has more followers A or B?").lower()



    #? Check if user is correct.
    ## Get follower count of each account.
    a_flwr_cnt = account_a["follower_count"]
    b_flwr_cnt = account_a["follower_count"]

    is_correct = check_answer(guess, a_flwr_cnt, b_flwr_cnt)

    #? Give user feedback on their guess.
    #? Score keeping.
    if is_correct:
        
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False



    #? Make the game repeatable.

    #? Makin account at position B become the next accoun at position A.

    #? Clear the screen between rounds.

