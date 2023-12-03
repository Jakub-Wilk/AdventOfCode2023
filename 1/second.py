import re

with open("input.txt", "r") as f:
    lines = f.readlines()
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits: list[str] = [
    re.findall(rf"(?=({'|'.join(digit_words)}|\d))", line) for line in lines
]
digits_converted = [
    [s if s.isnumeric() else str(digit_words.index(s) + 1) for s in digitset]
    for digitset in digits
]
answer = sum([int(digitset[0] + digitset[-1]) for digitset in digits_converted])
print(answer)
