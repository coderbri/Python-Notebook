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
is_game_over = False

# ? TODO 8: Define the score variables here to prevent them from being undefined
computer_score = -1
user_score = -1

for _ in range(2):
	user_deck.append(deal_card())
	computer_deck.append(deal_card())

# print(user_deck)        # Ex Output: [8, 9]
# print(computer_deck)    # Ex Output: [10, 10]

while not is_game_over:
    
    user_score = calculate_score(user_deck)             # Ex Output: 17
    computer_score = calculate_score(computer_deck)     # Ex Output: 20
    print(f"    Your cards: {user_deck}, current score: {user_score}")
    print(f"    Computer's first card: {computer_deck[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_deck.append(deal_card())
        else:
            is_game_over = True

# TODO 8: The score will need to be rechecked with every new card drawn and the
#   checks in TODO 6 need to be repeated until the game ends.

# TODO 9: Once the user is done, it's time to let the computer play. The computer should keep drawing
#   cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
    computer_deck.append(deal_card())
    computer_score = calculate_score(computer_deck) # contains updated score
