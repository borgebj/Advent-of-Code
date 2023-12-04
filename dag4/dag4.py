# borgebj
# part of Advent of code 2023 day 4
# https://adventofcode.com/2023/day/2


def extract_data(inp_file: str):
    """
    param:
        input (string): name of input-file
    return:
        int: sum of winnings
    """
    with open(inp_file) as file:
        lookup = {}
        file.seek(0)

        for line in file:
            # retrieves information from each line
            card, numbers = line.split(":")
            card_nr = int(card.split()[1])
            wining, owned = numbers.split("|")
            win_list = wining.split()
            own_list = owned.split()

            # creates the lookup list in the form of: {card: [card, ...], ...}
            ant_winning = sum(1 for x in own_list if x in win_list)
            lookup[card_nr] = [card_nr + i + 1 for i in range(ant_winning)]

    return lookup


def part_one(lookup: dict):
    lookup = [2 ** (len(lookup[key]) - 1) if lookup[key] else 0 for key in lookup]
    return sum(lookup)


def count_cards(copies, lookup, lookup_sum):
    # base case: no copies left
    if not copies or isinstance(copies, int):
        return lookup_sum

    # recursion step: count copies
    for card in copies:
        lookup_sum[card] += 1
        count_cards(lookup[card], lookup, lookup_sum)


def part_two(lookup: dict):
    lookup_sum = {i + 1: 1 for i in range(len(lookup))}

    # counts copies for each of the cards based on winning
    for key, copies in lookup.items():
        count_cards(copies, lookup, lookup_sum)

    return sum(lookup_sum.values())


winnings = extract_data("input.txt")
total_cards = part_two(winnings)

print("part one:", part_one(winnings))
print("part two:", total_cards)
