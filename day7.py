cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
cards_joker = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


# Open input and return the lines
def open_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


# Determine the strength of the hand and cards
def determine_strength(hand, bid):
    strength = 0

    # Determine the strength of the hand
    if len(set(hand)) == 1:
        strength = 6
    else:
        for card in set(hand):
            if hand.count(card) == 4:
                strength = 5
                break
            elif hand.count(card) == 3 and len(set(hand)) == 2:
                strength = 4
                break
            elif hand.count(card) == 3:
                strength = 3
                break
            elif hand.count(card) == 2 and len(set(hand)) == 3:
                strength = 2
                break
            elif hand.count(card) == 2 and len(set(hand)) == 4:
                strength = 1
                break

    # Calculate every card's individual value into a list
    i_strength = []
    for card in hand:
        i_strength.append(cards.index(card) + 1)

    return [strength, i_strength, bid]


# Determine the best strength of the hand and cards
def determine_strength_with_joker(hand, bid):
    strength = [0]
    joker_amount = hand.count("J")
    cards_set = set(hand.replace("J", ""))
    card_amount = len(cards_set)

    if joker_amount >= 4:
        strength.append(6)
    else:
        for card in cards_set:
            if hand.count(card) + joker_amount == 5:
                strength.append(6)
            elif hand.count(card) + joker_amount == 4:
                strength.append(5)
            elif card_amount == 2 and hand.count(card) + joker_amount == 3:
                strength.append(4)
            elif card_amount == 3 and hand.count(card) + joker_amount == 3:
                strength.append(3)
            elif card_amount == 3 and hand.count(card) + joker_amount == 2:
                strength.append(2)
            elif card_amount == 4 and hand.count(card) + joker_amount == 2:
                strength.append(1)

    strength.sort(reverse=True)
    strength = strength[0]

    # Calculate every card's individual value into a list
    i_strength = []
    for card in hand:
        i_strength.append(cards_joker.index(card) + 1)

    return [strength, i_strength, bid]


# Part 1: Total winnings no joker.
def part1(_input):
    result = 0

    # List containing 7 other lists. (other lists are for the hand strengths,
    # with the first one being for high cards and the last one for five of a kind.)
    sorted_cards = [[], [], [], [], [], [], []]

    # Calculate hand and individual card strength into a list
    for line in _input:
        hand, bid = line.split()
        strength = determine_strength(hand, int(bid))
        sorted_cards[strength[0]].append([strength[1], strength[2]])

    # Sort the lists using individual card strengths and calculate the total winnings.
    i = 1
    for card in sorted_cards:
        card.sort()

        for data in card:
            result += data[1] * i
            i += 1

    return result


# Part 2: total winnings with joker.
def part2(_input):
    result = 0

    # List containing 7 other lists. (other lists are for the hand strengths,
    # with the first one being for high cards and the last one for five of a kind.)
    sorted_cards = [[], [], [], [], [], [], []]

    # Calculate hand and individual card strength into a list
    for line in _input:
        hand, bid = line.split()
        strength = determine_strength_with_joker(hand, int(bid))
        sorted_cards[strength[0]].append([strength[1], strength[2]])

    # Sort the lists using individual card strengths and calculate the total winnings.
    i = 1
    for card in sorted_cards:
        card.sort()

        for data in card:
            result += data[1] * i
            i += 1

    return result


# Run
if __name__ == "__main__":
    inp = open_input("day7.txt")

    print(
        "Part 1:",
        part1(inp),
        "Part 2:",
        part2(inp),
        sep="\n"
    )
