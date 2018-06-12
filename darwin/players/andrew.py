import random

from abstract import AbstractPlayer


class AndrewPlayer(AbstractPlayer):
    # You have
    # self.turn - current turn, starting from zero
    # self.history - [(2,3), (3, 3), (4, 3), ..., (1, 4)] - history of your battles, (x, y) x - yours, y - his
    # make_decision - the only method you should implement

    def make_decision(self):
        if self.turn == 0:
            return 5

        if self.history[0][1] == 5:
            my_previous_turn, his_previous_turn = self.history[self.turn - 1]
            if my_previous_turn == his_previous_turn:
                return random.choice([2, 3])

            return self.history[self.turn - 1][1]

        else:
            return 3
