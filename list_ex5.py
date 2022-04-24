# create a list that represents a deck of cards, from A, 1-10,J,Q,K
# get the hightest cards giving a input of a card names

card_numbers=[str(i) for i in range(2,11)]

card_numbers.insert(0,'A')
card_letters=['J','Q','K']
card_deck=card_numbers+card_letters
selected_card=input("elije una carta entre A,2-10,J,Q,K:")
selected_card_index= card_deck.index(selected_card)

print("las cartas mayores son:",card_deck[selected_card_index+1:])
