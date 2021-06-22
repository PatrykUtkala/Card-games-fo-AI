from Cards import Deck
import Cards
import Games
import random


class DeckHandler:
    def __init__(self, deck=None):
        if deck is None:
            deck = Deck()
        self.deck = deck

    def shuffle_deck(self):
        random.shuffle(self.deck.deck_list)

    def print_deck(self):
        for card in self.deck.deck_list:
            print(card.suit, card.type)


def check_deck():
    D = Deck(joker_count=2)
    DH = DeckHandler(deck=D)
    DH.print_deck()
    DH.shuffle_deck()
    print("Deck Shuffled")
    DH.print_deck()


def check_war():
    D = Deck(card_list=Cards.cards_less)
    war = Games.War(D)
    war.play_game()

check_war()
