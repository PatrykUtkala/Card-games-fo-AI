import random

suits = ["Diamonds", "Hearths", "Spades", "Clubs"]
cards_normal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards_less = ["9", "10", "Jack", "Queen", "King", "Ace"]
jokers = ["Joker"]


class Card:
    """
    Card class with it's type and suit
    """
    def __init__(self, card_type="Ace", suit="Hearths"):
        """
        :param card_type: string naming that card
        :param suit: string naming suit of the card
        """
        self.type = card_type
        self.suit = suit


class Deck:
    def __init__(self, card_list=None, used_suits=None, joker_count=0):
        """
        :param card_list: List of cards to be used, if none full set is used
        :param used_suits: List of suits cards can have, if none all 4 suits are used
        :param joker_count: Amount of jokers in the pool
        """
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
        """
        Shuffles deck list
        """
        random.shuffle(self.deck_list)

    def put_at_bottom(self, card):
        """
        Puts card at the bottom of the deck

        :param card: card to be put at bottom
        """
        self.deck_list.insert(0, card)

    def take_from_top(self):
        """
        Returns card from top of the deck removing it in the process

        :return: card object
        """
        return self.deck_list.pop()

    def put_at_top(self, card):
        """
        Puts card at the top of the deck

        :param card: card to be put at top
        """
        self.deck_list.insert(len(self.deck_list), card)




