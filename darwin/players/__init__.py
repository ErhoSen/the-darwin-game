from players.andrew import AndrewPlayer
from players.full_random import FullRandomPlayer
from players.rocket import RocketPlayer
from players.dumb import DumbPlayer
from players.mimic import MimicPlayer
from players.two import TwoPlayer

players_list = [AndrewPlayer, DumbPlayer, RocketPlayer, TwoPlayer, FullRandomPlayer]

__all__ = (
    'players_list'
)
