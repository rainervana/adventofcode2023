import re
import numpy as np
# Day 3: Gear Ratios

# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# Part 1
def part1(_input):
    result = 0

    # Find the numbers with positions.
    numbers = []
    for index, row in enumerate(_input):
        digits = re.finditer(r"\d+", row)

        for match in digits:
            numbers.append([match.group(), match.span(), index])

    # Grid
    grid = []
    for line in _input:
        grid.append([*line])

    np_grid = np.array(grid)

    # Check which numbers have a symbol next to them
    part_numbers = []
    for number_info in numbers:
        number = number_info[0]
        col_start = number_info[1][0]
        col_end = number_info[1][1]
        row = number_info[2]
        add = False

        for c in range(col_start, col_end):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        if not np_grid[row + i, c + j].isnumeric() and np_grid[row + i, c + j] != ".":
                            add = True
                    except IndexError:
                        pass

        if add is True:
            part_numbers.append(number)

    # Add them together.
    for num in part_numbers:
        result += int(num)

    return result


# Part 2
def part2(_input):
    result = 0

    # Find the numbers with positions.
    numbers = []
    for index, row in enumerate(_input):
        digits = re.finditer(r"\d+", row)

        for match in digits:
            numbers.append([match.group(), match.span(), index])

    # Grid
    grid = []
    for line in _input:
        grid.append([*line])

    np_grid = np.array(grid)

    # Check which numbers have a symbol next to them
    part_numbers = []
    gears = {}
    for number_info in numbers:
        number = number_info[0]
        col_start = number_info[1][0]
        col_end = number_info[1][1]
        row = number_info[2]

        for c in range(col_start, col_end):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        if not np_grid[row + i, c + j].isnumeric() and np_grid[row + i, c + j] != ".":
                            if np_grid[row + i, c + j] == "*":
                                if not "{0},{1}".format(row + i, c + j) in gears:
                                    gears["{0},{1}".format(row + i, c + j)] = [number]
                                else:
                                    if not number in gears["{0},{1}".format(row + i, c + j)]:
                                        gears["{0},{1}".format(row + i, c + j)].append(number)
                    except IndexError:
                        pass

    # Add gear numbers together.
    for gear in gears.values():
        if len(gear) != 1:
            result += int(gear[0]) * int(gear[1])

    return result


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
