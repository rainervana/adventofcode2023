import re


# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# Part 1
def part1(_input):
    # Just loops through and checks if any of the cubes are over the allowed size.
    result = 0

    for line in _input:
        data = re.sub("[:;,]", "", line).split()
        valid = True

        for i in range(len(data)):
            if data[i] == "red":
                if int(data[i-1]) > 12:
                    valid = False
            elif data[i] == "green":
                if int(data[i-1]) > 13:
                    valid = False
            elif data[i] == "blue":
                if int(data[i-1]) > 14:
                    valid = False

        if valid:
            result += int(data[1])

    return result


# Part 2
def part2(_input):
    # Loops through and finds the largest value.
    result = 0

    for line in _input:
        data = re.sub("[:;,]", "", line).split()
        red = green = blue = 0

        for i in range(len(data)):
            if data[i] == "red":
                if int(data[i-1]) > red:
                    red = int(data[i-1])
            elif data[i] == "green":
                if int(data[i - 1]) > green:
                    green = int(data[i - 1])
            elif data[i] == "blue":
                if int(data[i - 1]) > blue:
                    blue = int(data[i - 1])
        result += red * green * blue

    return result


# Run
if __name__ == "__main__":
    inp = open_input("inputs/day2.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )

