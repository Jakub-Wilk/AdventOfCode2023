import re

with open("input.txt", "r") as f:
    games = f.readlines()
powers = [
    max([int(match) for match in re.findall("\d+(?= r)", game)])
    * max([int(match) for match in re.findall("\d+(?= g)", game)])
    * max([int(match) for match in re.findall("\d+(?= b)", game)])
    for game in games
]
print(sum(powers))
