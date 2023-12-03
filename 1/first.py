import re

with open("input.txt", "r") as f:
    lines = f.readlines()
digits = [re.findall(r"\d", line) for line in lines]
answer = sum([int(digitset[0] + digitset[-1]) for digitset in digits])
print(answer)
