# the-darwin-game
Python implementation of the Darwin Game.

Rules from the thezvi blogpost, can be found here

https://thezvi.wordpress.com/2017/11/15/the-darwin-game/

Short quote:

```
Each turn, each player simultaneously submits an integer number from 0 to 5.
If the two numbers add up to 5 or less, each player earns points equal to their own number.
If the two numbers add up to 6 or more, neither player gets points.
This game then lasts for a large but unknown number of turns, so no one knows when the game is about to end;
for us this turned out to be 102 turns.

Each pairing is independent of every other pairing.
You do not know what round of the game it is, whether you are facing a copy of yourself,
or any history of the game to this point. Your decision algorithm does the same thing each pairing.
You do know the results of previous turns in the same pairing.

At the end of the round, all of the points scored by all of your copies are combined.
Your percentage of all the points scored by all programs becomes the percentage of the pool
your program gets in the next round. So if you score 10% more points, you get 10% more copies next round,
and over time successful programs will displace less successful programs. Hence the name, The Darwin Game.

Your goal is to have as many copies in the pool at the end of the 200th round as possible, or failing that,
to survive as many rounds as possible with at least one copy.
```

Requirements:
python 3.6

How to run:

`python darwin/stand.py`

List of players, participated in competition, can be found here:
`darwin/players/__init__.py`

Write your own bot, create MR and try to win other players!
