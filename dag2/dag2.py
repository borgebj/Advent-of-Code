# borgebj
# part of Advent of code 2023 day 2
# https://adventofcode.com/2023/day/2


def part_one(inp_file):
    """
    param:
        input (string): name of input-file
    return:
        int: sum of IDs
    """
    with open(inp_file) as inp:
        id_sum = 0

        for line in inp:

            # dict to hold colors for each game
            colors = {"red": 0, "green": 0, "blue": 0}

            # seperates the game ID and the game
            colon = line.index(":")
            rest = line[colon + 2:]
            game_id = int(line[:colon].split()[1])
            valid_game = True

            # iterates through each game-set
            for game_set in rest.split(";"):
                cubes = game_set.split(",")

                # iterates through each cube and its color for each set
                for cube in cubes:
                    cubeline = cube.strip().split()
                    num = int(cubeline[0])
                    col = cubeline[1].lower()
                    colors[col] = num

                    # invalid game if these criteria are met
                    if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
                        valid_game = False

            # adds sum if valid game ↑
            if valid_game:
                id_sum += game_id

        return id_sum


col_sum = part_one("input.txt")
print("part one:", col_sum)


def part_two(inp_file):
    """
    param:
        input (string): name of input-file
    return:
        int: sum of IDs
    """
    inp = open(inp_file)
    id_sum = 0

    for line in inp:

        # dict to hold colors for each game
        colors = {"red": 0, "green": 0, "blue": 0}

        # separates the game ID and the game
        colon = line.index(":")
        rest = line[colon + 2:]

        # iterates through each game-set
        for game_set in rest.split(";"):
            cubes = game_set.split(",")

            # iterates through each cube and its color for each set
            for cube in cubes:
                cubeline = cube.strip().split()
                num = int(cubeline[0])
                col = cubeline[1].lower()

                # saves only the highest number
                if num > colors[col]:
                    colors[col] = num

        # calculates the power of the cubes
        power = colors["red"] * colors["green"] * colors["blue"]
        id_sum += power

    return id_sum


pow_sum = part_two("input.txt")
print("part two:", pow_sum)
