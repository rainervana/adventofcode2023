# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# Formats the data into a list [winning_numbers, numbers_you_have]
def format_game(_input):
    result = []

    for r, line in enumerate(_input):
        line = line.split(":")[1]
        a, b = line.split("|")
        a, b = a.split(), b.split()

        result.append([a, b])

    return result


# Calculates the game points
def get_game_points(game):
    game_points = 0

    # Get matching numbers
    matching = set(game[0]) & set(game[1])
    if len(matching) > 0:
        game_points = 2 ** (len(matching) - 1)

    return game_points


# Part 1: check if winning numbers match the numbers you have and then add the points.
def part1(_input):
    result = 0
    game_data = format_game(_input)

    for game in game_data:
        result += get_game_points(game)

    return result


# Part 2:
def part2(_input):
    game_data = format_game(_input)
    cards = []
    index = 0

    for _ in game_data:
        cards.append(1)

    for game in game_data:
        matching = len(set(game[0]) & set(game[1]))

        for i in range(matching):
            cards[index + i + 1] += cards[index]

        index += 1

    return sum(cards)


# Run
if __name__ == "__main__":
    inp = open_input("day4.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )
