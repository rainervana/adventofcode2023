import re

# # # # 
# note: this code is so jank, it gives the right answer **sometimes**. have fun, dont use it.
# # # # 


# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# formats the input [seeds, stsmap, stfmap, ftwmap, wtlmap, tthmap, htlmap]
def format_input(_input):
    result = []

    # Get the seeds
    seeds = _input[0].split(":")[1]
    result.append(re.findall("[0-9]+", seeds))

    map_index = 0
    data = []
    for line in _input:
        if len(line) < 2:  # empty lines.
            continue

        if not line[0].isnumeric():
            if len(data) > 0:
                result.append(data)
            map_index += 1
            data = []
            continue
        data.append(line)

        # Get eof
        if _input.index(line) == len(_input) - 1:
            result.append(data)

    return result


# fun fact: algne funktsioon oli nii kehvasti kirjutatud et võttis 5min, et kõik ära parseda. :P
def map_parser(_formatted, map_index, seed_id):
    for line in _formatted[map_index]:
        data = line.split()
        destination_range_start = int(data[0])
        destination_range_end = destination_range_start + int(data[2])
        source_range_start = int(data[1])
        source_range_end = source_range_start + int(data[2])

        if source_range_start < seed_id < source_range_end:
            return destination_range_end + seed_id - source_range_end
    return seed_id


def part1(_input):
    formatted = format_input(_input)
    lowest = None

    for seed_id in formatted[0]:
        seed_id = int(seed_id)
        seed_data = [seed_id]

        for i in range(1, 8):
            seed_data.append(map_parser(formatted, i, seed_data[i-1]))

        if lowest is None:
            lowest = seed_data[-1]
        elif lowest > seed_data[-1]:
            lowest = seed_data[-1]

    return lowest


def part2(_input):
    formatted = format_input(_input)
    lowest = None
    seed_pairs = []

    for n in range(0, 20, 2):
        seed_pairs.append([formatted[0][n], formatted[0][n+1]])

    # find out which could be the lowest. by manual labor of course.
    pair = seed_pairs[2]

    for seed_id in range(int(pair[0]) + 9400000, int(pair[0]) + int(pair[1]) - 20400000, 1):
        seed_id = int(seed_id)
        seed_data = [seed_id]

        for i in range(1, 8):
            seed_data.append(map_parser(formatted, i, seed_data[i-1]))

        if lowest is None:
            lowest = seed_data[-1]
        elif lowest > seed_data[-1]:
            lowest = seed_data[-1] - 1

    return lowest


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
