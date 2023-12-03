#
with open(r"C:\Users\Lars Rikard\Documents\GitHub\adventofcode\2023\day2\day2_input.txt") as gamedata:
    games = [line.strip("\n") for line in gamedata]

for g in games[0:5]:
    print(g)