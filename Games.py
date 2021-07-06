import random

import Cards
import numpy as np
from collections import Counter


class Game:
    def __init__(self, deck, players, viewer):
        self.deck = deck
        self.players = players
        self.viewer = viewer

    def play_turn(self):
        """
        :return: True if game is finished
        """
        return True

    def cleanup(self):
        return self.deck


class War:
    """
    Game "War"
    Rules:
    """

    def __init__(self, deck, players_count=2):
        self.weights = {}
        for card_type_counter in range(len(Cards.cards_normal)):
            self.weights[Cards.cards_normal[card_type_counter]] = card_type_counter

        self.deck = deck
        self.players = players_count
        self.piles = []
        for i in range(players_count):
            self.piles.append([])

    def play_game(self):
        """
        Plays War and prints state of the game.
        :return: None
        """
        self.deck.shuffle()
        turn = 0
        for card_counter in range(len(self.deck.deck_list)):
            self.piles[card_counter % self.players].append(self.deck.deck_list[card_counter])

        while self.check_finish():
            turn += 1
            field = []
            for player in range(self.players):
                print("Player <" + str(player) + "> places:", self.piles[player][-1].type)
                field.append(self.weights[self.piles[player][-1].type])

            # if [item for item, count in Counter(field).items() if count > 1]:
            #     for player in range(self.players):
            #         self.piles[player].pop()
            # else:
            winner = np.argmax(field)
            take_cards = []
            for player in range(self.players):
                take_cards.append(self.piles[player].pop())

            for card in take_cards:
                self.piles[winner].insert(0, card)
            print("Player <" + str(winner) + "> takes pile", "Player 0 Cards:",
                  len(self.piles[0]), "Player 1 Cards:", len(self.piles[-1]), "turn:", turn)
            for player in range(self.players):
                random.shuffle(self.piles[player])

    def check_finish(self):
        """
        :return: True if game should continue, False otherwise
        """
        not_empty_counet = 0
        for pile in self.piles:
            if len(pile) > 0:
                not_empty_counet += 1

        if not_empty_counet > 1:
            return True
        return False


class Makao(Game):
    def __init__(self, players, viewer, jokers=0):
        """
        Game is played with same deck with different number of Jokers
        
        :param players: list of Player objects
        :param viewer:  viewer object od the Game
        :param jokers:  number of Jokers to be put
        """
        deck = Cards.Deck(joker_count=jokers)
        super().__init__(deck, players, viewer)
        self.deck.shuffle()
        self.hands = []
        self.pile = []
        for player in players:
            hand = []
            for i in range(5):
                hand.append(self.deck.deck_list.pop())
            self.hands.append(hand)
        while True:
            self.pile.append(self.deck.deck_list.pop())
            if self.pile[0].type in ["5", "6", "7", "8", "9", "10"]:
                break
            self.deck.put_at_bottom(self.pile.pop())

    def play_turn(self):
        """
        play single turn of the game for all players

        :return: True if game is finished, False otherwise
        """
        for i in range(len(self.players)):
            pile_top = self.pile[-1]

        for hand in self.hands:
            if len(hand) != 0:
                return False
        return True
