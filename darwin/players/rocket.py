import random

from abstract import AbstractPlayer


class RocketPlayer(AbstractPlayer):
    # You have
    # self.turn - current turn, starting from zero
    # self.history - [(2,3), (3, 3), (4, 3), ..., (1, 4)] - history of your battles, (x, y) x - yours, y - his
    # make_decision - the only method you should implement

    def make_decision(self):
        my_signal = [2, 3, 2]
        if self.turn < 3:
            return my_signal[self.turn]

        his_signal = [his for my, his in self.history[:3]]
        copy_of_myself = his_signal == my_signal

        if self.turn > 3:
            my_previous_turn, his_previous_turn = self.history[self.turn - 1]
            if copy_of_myself:
                if my_previous_turn + his_previous_turn == 5:
                    return my_previous_turn
            else:
                if my_previous_turn == his_previous_turn:
                    return random.choice([2, 3])

        return random.choice([2, 3])
