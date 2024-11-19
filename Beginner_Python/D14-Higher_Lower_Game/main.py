# TODO 1: Import required modules: art, random and game data
import random
from art import logo, vs
from game_data import data

# ✓ TODO 2: Randomly select an account from the game data.
#    1. Import random module and use random.choice() to choose a dictionary entry.
#    2. Ensure that the second generated account is different from the first.
def select_account(list_of_dicts):
    return random.choice(data)

# ✓ TODO 3: Format the account data into a printable format.
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, from {account_country}."

# ✓ TODO 5.2: Use if statement to check if user is correct.
def check_answer(user_guess, a_followers, b_followers):
    """Takes the user's guess as well as the follower counts and returns if the user got it right."""
    # 1. Compare the follower accounts
    if a_followers > b_followers:
        return user_guess == "a" # if valid, return True
    else:
        return user_guess == "b" # if invalid, return False


print(logo)

# ✓ TODO 5.4: Keep score.
score = 0
# ✓ TODO 6.2: Makes game repeatable until user makes a wrong choice, exiting the True statement.
game_should_continue = True
# ✓ TODO 7.2: Initialize account_b to be account_a
account_b = select_account(data)

# ✓ TODO 6: Make Game Repeatable. Think about what part of the game should repeat itself.
while game_should_continue:
    
    # ✓ TODO 7: Reassign account in position 'B' to position 'A'.
    account_a = account_b
    account_b = select_account(data)

    if account_a == account_b:
        account_b = select_account(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    # ✓ TODO 4: Ask user for guess and assign to choices 'A' or 'B'.
    #    1. Check for edge-cases to validate the user's input.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # ✓ TODO 8: Clear screen and reprint logo.
    print("\n" * 20)
    print(logo)

    # ✓ TODO 5: Check if user is correct.
    #    1. Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    #   2. Use if statement to check if user is correct.
    #   3. Give user feedback on their guess. End game if user is right, otherwise continue game.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        #   4. Score Keeping.
        score += 1
        print(f"You're Right! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_should_continue = False
