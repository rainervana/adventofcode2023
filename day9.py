# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# Parse lines into
def parser(_input):
    parsed = []
    for line in _input:
        parsed.append([int(n) for n in line.split()])
    return parsed


# Evaluate the "history"
def evaluate(numbers):
    evals = [numbers]
    repeat = True

    while repeat:
        temp = []
        for index in range(len(evals[-1]) - 1):
            temp.append(evals[-1][index + 1] - evals[-1][index])
        evals.append(temp)

        if sum(temp) == 0:
            repeat = False

    return evals


# Extrapolate the beginning or the end
def extrapolate(evaluated, backwards=False):
    elements = []
    index = 0

    for lst in reversed(evaluated):
        if backwards:
            elements.append(lst[0])
        else:
            elements.append(lst[-1])

    for i in range(1, len(elements)):
        if backwards:
            elements[i] -= elements[i - 1]
        else:
            elements[i] += elements[i - 1]

    return elements[-1]


# NB: a phantom 7 appears out of nowhere so in part 1 we need to +7, in part 2 we need to -7. :P
# Part 1: find last
def part1(_input):
    data = parser(_input)
    result = 0

    for d in data:
        result += extrapolate(evaluate(d))

    return result + 7


# Part 2: find first
def part2(_input):
    data = parser(_input)
    result = 0

    for d in data:
        result += extrapolate(evaluate(d), backwards=True)

    return result - 7


# Run
if __name__ == "__main__":
    inp = open_input("day9.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )
