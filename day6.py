import re
from numpy import prod


# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read()


# Returns data in a list
def parser(_input):
    return [re.findall("[0-9]+", _input.split(":")[1]), re.findall("[0-9]+", _input.split(":")[2])]


# How many wins are possible in the race.
def get_wins_possible(time, record):
    wins = 0

    for hold_time in range(1, time):
        if hold_time * (time - hold_time) > record:
            wins += 1

    return wins


# Part 1: calculate the wins possible using all the races
def part1(_input):
    data = parser(_input)
    wins = []

    for index in range(len(data[0])):
        wins.append(get_wins_possible(int(data[0][index]), int(data[1][index])))

    return prod(wins)


# Part 2: add the numbers together for a big race and then calculate how many ways can you win.
def part2(_input):
    data = parser(_input)

    time = int("".join(data[0]))
    record = int("".join(data[1]))

    return get_wins_possible(time, record)


# Run
if __name__ == "__main__":
    inp = open_input("input.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )
