import random

# TODO 1: Create a deal_card() function that returns a random card from the `cards` list
def deal_card():
	"""Using `random.choice(cards)`, a random card is retrieved from the deck."""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	chosen_card = random.choice(cards)
	return chosen_card

# TODO 2: Deal the user and the computer two cards each using `deal_card()` and `.append()`
user_deck = []
computer_deck = []

for _ in range(2):
	user_deck.append(deal_card())
	computer_deck.append(deal_card())

print(user_deck)        # Ex Output: [8, 9]
print(computer_deck)    # Ex Output: [10, 10]
