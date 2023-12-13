import numpy as np

tiles = ["|", "-", "L", "J", "7", "F"]


# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


def determine_next_step(current_pos, last_pos, current_tile):
    possible_steps = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    if current_tile == "|":
        if current_pos[0] > last_pos[0]:
            return possible_steps[2]  # go down
        else:
            return possible_steps[0]  # go up
    elif current_tile == "L":
        if current_pos[0] > last_pos[0]:
            return possible_steps[3]  # go right
        else:
            return possible_steps[0]  # go up
    elif current_tile == "J":
        if current_pos[1] > last_pos[1]:
            return possible_steps[0]  # go up
        else:
            return possible_steps[1]
    elif current_tile == "F":
        if current_pos[0] < last_pos[0]:
            return possible_steps[3]  # go right
        else:
            return possible_steps[2]  # go down
    elif current_tile == "-":
        if current_pos[1] > last_pos[1]:
            return possible_steps[3]  # go right
        else:
            return possible_steps[1]  # go left
    elif current_tile == "7":
        if current_pos[0] < last_pos[0]:
            return possible_steps[1]  # go left
        else:
            return possible_steps[2]  # go down

    print("unknown tile?!? bye.", current_pos, last_pos, current_tile, "[current pos, last pos, tile]", sep="\n")
    exit()


# Make the array into a grid.
def numpify(_input):
    filler = "." * (len(_input) + 2)
    arr = []
    for line in _input:
        arr.append([".", *line, "."])
    arr.insert(0, [*filler])
    arr.append([*filler])

    return np.array(arr)


def find_furthest(arr):
    test_arr = np.full(arr.shape, ".")
    start_r, start_c = np.argwhere(arr == "S")[0]
    test_arr[start_r, start_c] = 'X'

    first_possible_steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    first_possible_starts = [["|", "7", "F"], ["|", "L", "J"], ["-", "L", "F"], ["-", "J", "7"]]

    current_pos = [[start_r, start_c], [start_r, start_c]]
    last_pos = [[start_r, start_c], [start_r, start_c]]
    current_steps = [0, 0]

    # Determine the first step
    for pos in current_pos:
        current = current_pos.index(pos)
        current_r = pos[0]
        current_c = pos[1]

        for step in first_possible_steps:
            next_tile = arr[current_r + step[0], current_c + step[1]]

            # Check for impossible start.
            if next_tile not in first_possible_starts[first_possible_steps.index(step)]:
                continue

            # Make the first step
            if arr[current_r + step[0], current_c + step[1]] in tiles:
                current_steps[current] += 1
                current_pos[current] = [current_r + step[0], current_c + step[1]]
                last_pos[current] = [current_r, current_c]

                del first_possible_starts[first_possible_steps.index(step)]
                first_possible_steps.remove(step)

                test_arr[current_r + step[0], current_c + step[1]] = "X"
                break

    # Now start stepping.
    run = True

    while run:
        for pos in current_pos:
            current = current_pos.index(pos)

            current_r = pos[0]
            current_c = pos[1]

            step = determine_next_step([pos[0], pos[1]], last_pos[current], arr[current_r, current_c])

            current_steps[current] += 1
            pos[0], pos[1] = current_r + step[0], current_c + step[1]
            last_pos[current] = [current_r, current_c]
            test_arr[pos[0], pos[1]] = "X"

        if current_pos[0] == current_pos[1]:
            run = False

    return current_steps[0], test_arr


# Part 1: find the furthest point.
def part1(_input):
    arr = numpify(_input)

    return find_furthest(arr)[0]


# Part 2: not my finest code. but fills the empty areas with I then cleans it up.
def part2(_input):
    arr = numpify(_input)
    c_arr = find_furthest(arr)[1]
    size = c_arr.shape[0]
    end = 0

    for m in range(4):
        for r in range(1, size - 1):
            for c in range(1, size - 1):
                if c_arr[r, c] == ".":
                    if c_arr[r + 1, c] == "X":
                        c_arr[r, c] = "I"
                    if c_arr[r - 1, c] == "X":
                        c_arr[r, c] = "I"
                    if c_arr[r, c + 1] == "X":
                        c_arr[r, c] = "I"
                    if c_arr[r, c - 1] == "X":
                        c_arr[r, c] = "I"

    for m in range(10):
        for r in range(1, size - 1):
            for c in range(1, size - 1):
                if c_arr[r, c] == "I":
                    if c_arr[r - 1, c] not in "IX":
                        c_arr[r, c] = "."
                    if c_arr[r + 1, c] not in "IX":
                        c_arr[r, c] = "."
                    if c_arr[r, c - 1] not in "IX":
                        c_arr[r, c] = "."
                    if c_arr[r, c + 1] not in "IX":
                        c_arr[r, c] = "."

    for r in range(1, size - 1):
        for c in range(1, size - 1):
            if c_arr[r, c] == "I":
                end += 1

    return end


# Run
if __name__ == "__main__":
    inp = open_input("day10.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )
