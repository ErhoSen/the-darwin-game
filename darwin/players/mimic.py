import random

from abstract import AbstractPlayer


class MimicPlayer(AbstractPlayer):
    # You have
    # self.turn - current turn, starting from zero
    # self.history - [(2,3), (3, 3), (4, 3), ..., (1, 4)] - history of your battles, (x, y) x - yours, y - his
    # make_decision - the only method you should implement

    def make_decision(self):
        if self.turn == 0:
            return random.choice([2, 3])

        return self.history[self.turn - 1][1]
