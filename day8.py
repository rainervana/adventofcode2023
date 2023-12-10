import math


# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# Parse lines into [instructions, node, network_nodes]
def parser(_input):
    final = [[*_input[0].translate(str.maketrans("LR", "01"))], [], []]

    for line in _input[2:]:
        index = line.split("=")[0][:3]
        nodes = line.split("=")[1].replace(" ", "")[1:-1].split(",")

        final[1].append(index)
        final[2].append(nodes)

    return final


# Part 1: AAA to ZZZ.
def part1(_input):
    network = parser(_input)
    current_index = network[1].index("AAA")  # find AAA index in list
    end_index = network[1].index("ZZZ")  # find ZZZ index in list
    searching = True
    steps = 0

    while searching:
        for direction in network[0]:
            current_index = network[1].index(network[2][current_index][int(direction)])
            steps += 1

            # Check if AAA index and ZZZ index match, if so end.
            if current_index == end_index:
                searching = False
                break

    return steps


# Part 2: all the XXA to XXZ.
def part2(_input):
    network = parser(_input)
    start_indexes = []
    end_indexes = []
    index_steps = []  # how many steps did it take for every XXA to reach XXZ

    # Find every XXA and every XXZ.
    for node in network[1]:
        if node[2] == "A":
            start_indexes.append(network[1].index(node))
        elif node[2] == "Z":
            end_indexes.append(network[1].index(node))

    # Pretty much same as part 1, but puts the step count in index_steps.
    for i in range(len(start_indexes)):
        steps = 0
        searching = True
        current_index = start_indexes[i]

        while searching:
            for direction in network[0]:
                current_index = network[1].index(network[2][current_index][int(direction)])
                steps += 1

                if current_index in end_indexes:
                    searching = False
                    break

        index_steps.append(steps)

    # returns least common multiplier
    return math.lcm(*index_steps)


# Run
if __name__ == "__main__":
    inp = open_input("day8.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )
