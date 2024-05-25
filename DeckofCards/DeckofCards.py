# Jacob Heffington
# CIS261
# Deck of Cards

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Deck:
    def __init__(self):
        self.suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
        self.ranks = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
        self.deck = self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        while True:
            try:
                num_cards_to_deal = int(input("How many cards would you like? "))
                break
            except:
                pass
    
        dealt_cards = []
        
        for _ in range(num_cards_to_deal):
            if len(self.deck) == 0:
                print("No more cards in the deck.")
            else:
                card = self.deck.pop()
                dealt_cards.append(f'{card.rank} of {card.suit}')
        if dealt_cards:
            print("\nHere are your cards:")
            for card in dealt_cards:
                print(card)
    def count(self):
        remaining_count = len(self.deck)
        print(f'There are {remaining_count} cards in the deck.')
        print("\nGood luck!")

def main():
    print("Welcome to the card dealer\n")
    print("There is a deck of 52 cards.\n")
    deck = Deck()
    
    deck.deal()
            
    deck.count()

if __name__ == "__main__":
    main()