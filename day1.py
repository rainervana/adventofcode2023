import re


# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# Part 1
def part1(_input):
    # Gets digits in the line and combines the first and the last digit and in the end adds them all together.
    result = 0

    for line in _input:
        digits = re.findall("[0-9]", line)
        result += int(digits[0] + digits[-1])

    return result


# Part 2:
def part2(_input):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = 0

    # Convert string digits into normal digits
    # note: replaces the digit with digit string + int + digit string, so: 'one' will be replaced with 'one1one'.
    for i in range(len(_input)):
        for digit in digits:
            _input[i] = _input[i].replace(digit, digit + str(digits.index(digit) + 1) + digit)

    for line in _input:
        digits = re.findall("[0-9]", line)
        result += int(digits[0] + digits[-1])

    return result


# Run
if __name__ == "__main__":
    inp = open_input("inputs/day1.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )

