import random

from abstract import AbstractPlayer


class FullRandomPlayer(AbstractPlayer):
    # You have
    # self.turn - current turn, starting from zero
    # self.history - [(2,3), (3, 3), (4, 3), ..., (1, 4)] - history of your battles, (x, y) x - yours, y - his
    # make_decision - the only method you should implement

    def make_decision(self):
        return random.choice(range(6))
