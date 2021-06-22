import random

suits = ["Diamonds", "Hearths", "Spades", "Clubs"]
cards_normal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards_less = ["9", "10", "Jack", "Queen", "King", "Ace"]
jokers = ["Joker"]


class Card:
    def __init__(self, card_type="Ace", suit="Hearths"):
        self.type = card_type
        self.suit = suit


class Deck:
    def __init__(self, card_list=None, used_suits=None, joker_count=0):
        if card_list is None:
            card_list = cards_normal
        if used_suits is None:
            used_suits = suits
        self.deck_list = []
        for suit in used_suits:
            for card_type in card_list:
                self.deck_list.append(Card(card_type, suit))

        for joker in range(joker_count):
            self.deck_list.append(Card("Joker", "Joker"))

    def shuffle(self):
        random.shuffle(self.deck_list)




