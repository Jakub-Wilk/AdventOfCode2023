import re

with open("input.txt", "r") as f:
    games = f.readlines()
games_possible = [
    game.split(":")[0].split(" ")[1]
    for game in games
    if max([int(match) for match in re.findall("\d+(?= r)", game)]) <= 12
    and max([int(match) for match in re.findall("\d+(?= g)", game)]) <= 13
    and max([int(match) for match in re.findall("\d+(?= b)", game)]) <= 14
]
print(sum([int(game) for game in games_possible]))
