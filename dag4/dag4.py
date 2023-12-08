# borgebj
# part of Advent of code 2023 day 4
# https://adventofcode.com/2023/day/2


def extract_data(inp_file: str) -> dict:
    lookup = {}

    with open(inp_file) as file:
        for line in file:
            # Split the line once
            parts = line.split(":")
            card_nr = int(parts[0].split()[1])

            # Use sets for membership testing
            win_list = set(parts[1].split("|")[0].split())
            own_list = set(parts[1].split("|")[1].split())

            # Use list comprehension to create the lookup list
            ant_winning = sum(1 for x in own_list if x in win_list)
            lookup[card_nr] = [card_nr + i + 1 for i in range(ant_winning)]

    return lookup


def count_cards(copies: list, lookup: dict, lookup_sum: dict) -> None:
    # base case: no copies left
    if not copies or isinstance(copies, int):
        return

    # recursion step: count copies
    for card in copies:
        lookup_sum[card] += 1
        count_cards(lookup[card], lookup, lookup_sum)


# ---------------------------------------------------------------------------------------------------------------------#

# counts winning points by 1 for none and multiples of 2 for any
def part_one(lookup: dict) -> str:
    win_sum = sum([2 ** (len(v) - 1) for k, v in lookup.items() if len(v) > 0])
    return f'Part one: {win_sum}'


# counts copies for each of the cards based on winning
def part_two(lookup: dict) -> str:
    lookup_sum = {i + 1: 1 for i in range(len(lookup))}


    #------------------------------------------------------------------------------
    # TODO finn ut av dette, idk hvordan det fungerer
    data = {k: len(v) for k,v in lookup.items()}
    [print(str(k)+":", v, [k+i+1 for i in range(v)]) for k,v in data.items()]

    # score = [1] * len(lookup.items())
    # for c, wins in enumerate([len(v) for _, v in lookup.items()]):
    #     i, j = c + 1, c + 1 + wins
    #     score[i:j] = [x + score[c] for x in score[i:j]]
    # print(sum(score))
    #------------------------------------------------------------------------------


    for copies in lookup.values():
        count_cards(copies, lookup, lookup_sum)

    return f'Part two: {sum(lookup_sum.values())}'


winnings = extract_data("input.txt")
print(part_one(winnings))
print(part_two(winnings))
