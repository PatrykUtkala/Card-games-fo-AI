import random


class RandomPlayer:
    def move(self, moves, state):
        """
        :param moves: list of legal moves
        :param state: state of the current game
        :return: index of move in moves list
        """
        return random.randint(0, len(moves))


class InputPlayer(RandomPlayer):
    def move(self, moves, state):
        move = int(input("your move: "))
        return move
