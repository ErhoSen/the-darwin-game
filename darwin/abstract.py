class AbstractPlayer:

    def __init__(self):
        self.history = []

    def submit_result(self, my_decision, his_decision):
        self.history.append(
            (my_decision, his_decision)
        )

    def make_decision(self):
        raise NotImplemented

    @property
    def turn(self):
        return len(self.history)

    @classmethod
    def name(cls):
        return cls.__name__
