cards_deck = {'Jack': 11,
              'Queen': 12,
              'King': 13,
              'Ace': 14}

# Add numbered cards automatically
for num_card in range(2, 11):
    cards_deck[str(num_card)] = num_card

hand = [input() for _ in range(6)]

hand_avg = sum(cards_deck[card] for card in hand) / len(hand)
print(hand_avg)
