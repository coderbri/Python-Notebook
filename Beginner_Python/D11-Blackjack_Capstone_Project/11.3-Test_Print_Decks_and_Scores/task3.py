import random

def deal_card():
	"""Using `random.choice(cards)`, a random card is retrieved from the deck."""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	chosen_card = random.choice(cards)
	return chosen_card


def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


user_deck = []
computer_deck = []

for _ in range(2):
	user_deck.append(deal_card())
	computer_deck.append(deal_card())

# print(user_deck)        # Ex Output: [8, 9]
# print(computer_deck)    # Ex Output: [10, 10]


# TODO 6: Call `calculate_score()`. If the computer or user has a blackjack (0) or
#     if the user's score is over 21, then the game ends
user_score = calculate_score(user_deck)             # Ex Output: 17
computer_score = calculate_score(computer_deck)     # Ex Output: 20
print(f"    Your cards: {user_deck}, current score: {user_score}")
print(f"    Computer's first card: {computer_deck[0]}")

'''Ex Ouput:
    Your cards: [8, 9], current score: 17
    Computer's first card: 10
'''

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

# TODO 7: If the game has not ended, ask the user if they want to draw another card.
#   If yes, then use the deal_card() function to add another card to the user_cards List.
#   If no, then the game has ended.

# TODO 8: The score will need to be rechecked with every new card drawn and the
#   checks in Hint 9 need to be repeated until the game ends.
