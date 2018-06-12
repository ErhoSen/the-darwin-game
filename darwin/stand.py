import random

from players import players_list


NUMBER_OF_COPIES = 100
TOTAL_COPIES = len(players_list) * NUMBER_OF_COPIES


class DarwinGame:

    NUMBER_OF_TURNS = 102

    def __init__(self, darwin_players):
        self.darwin_players = darwin_players
        self.results = {
            darwin_player.player: 0
            for darwin_player in self.darwin_players
        }

    @property
    def player_to_darwin_map(self):
        return {
            darwin_player.player: darwin_player
            for darwin_player in self.darwin_players
        }

    def calculate_bonuses(self):
        total_points = sum(self.results.values())
        print(f"____ Total points: {total_points}")
        for player, result in self.results.items():
            player_percentage = result / total_points
            next_round_copies = round(player_percentage * TOTAL_COPIES)
            darwin_player = self.player_to_darwin_map[player]
            darwin_player.set_copies(next_round_copies)
            print(f"____ {darwin_player}: {result} points, {player_percentage} percentage")

        sum_of_copies = sum(d_player.copies for d_player in self.darwin_players)
        if sum_of_copies > TOTAL_COPIES:
            darwin_player_with_max_copies = max(self.darwin_players, key=lambda x: x.copies)
            darwin_player_with_max_copies.update_copies(-1)
        elif sum_of_copies < TOTAL_COPIES:
            darwin_player_with_min_copies = min(self.darwin_players, key=lambda x: x.copies)
            darwin_player_with_min_copies.update_copies(1)

    def run(self):
        pool = []
        for darwin_player in self.darwin_players:
            pool += darwin_player.spawn_copies()

        # shuffle pool
        random.shuffle(pool)

        # while there are something in the pool
        while pool:
            # get 2 random players from the pool
            p1 = pool.pop()()
            p2 = pool.pop()()

            p1_score, p2_score = 0, 0
            for turn in range(self.NUMBER_OF_TURNS):
                p1_decision, p2_decision = p1.make_decision(), p2.make_decision()
                # update the scores if possible
                if p1_decision + p2_decision <= 5:
                    p1_score += p1_decision
                    p2_score += p2_decision

                # submit turn results anyway
                p1.submit_result(my_decision=p1_decision, his_decision=p2_decision)
                p2.submit_result(my_decision=p2_decision, his_decision=p1_decision)

            # update total results
            self.results[p1.__class__] += p1_score
            self.results[p2.__class__] += p2_score

        return self.calculate_bonuses()


class DarwinPlayer:

    def __init__(self, player):
        self.player = player
        self.copies = NUMBER_OF_COPIES

    def set_copies(self, copies):
        self.copies = copies

    def update_copies(self, delta):
        self.copies += delta

    def spawn_copies(self):
        return [self.player] * self.copies

    def __str__(self):
        return f"{self.player.name()} copies: {self.copies}"


def main():
    darwin_players = []
    for player in players_list:
        darwin_players.append(DarwinPlayer(player))

    for i in range(200):
        print(f"\nDarwin game. Round {i}")
        [print(darwin_player) for darwin_player in darwin_players]

        game = DarwinGame(darwin_players=darwin_players)
        game.run()

        next_round_darwin_players = []
        for darwin_player in darwin_players:
            if darwin_player.copies == 0:
                print(f"{darwin_player.player.name()} loses!")
            else:
                next_round_darwin_players.append(darwin_player)

        darwin_players = next_round_darwin_players
        if len(darwin_players) == 1:
            print(f"\n{darwin_players[0].player.name()} won!")
            break
    else:
        print("Draw! \n")


if __name__ == '__main__':
    main()
