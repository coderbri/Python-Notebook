import random

def deal_card():
	"""Using `random.choice(cards)`, a random card is retrieved from the deck."""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	chosen_card = random.choice(cards)
	return chosen_card

user_deck = []
computer_deck = []

for _ in range(2):
	user_deck.append(deal_card())
	computer_deck.append(deal_card())

# print(user_deck)        # Ex Output: [8, 9]
# print(computer_deck)    # Ex Output: [10, 10]

# TODO 3: Create a function called calculate_score() that takes a List of cards as input
#   and returns the sum of all the cards in the List as the score.
def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards."""
    # TODO 4: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    #   and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # TODO 5: Inside calculate_score() check for an 11 (ace). If the score is
    #   already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

# print(calculate_score(user_deck))       # Ex Output: 17
# print(calculate_score(computer_deck))   # Ex Output: 20
