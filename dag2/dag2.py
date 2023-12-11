# borgebj
# part of Advent of code 2023 day 2
# https://adventofcode.com/2023/day/2

with open("input.txt") as f:
    data = f.read().splitlines()


def part_one(data):
    MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14
    id_sum = 0

    for line in data:

        # Extracts the game ID and the game
        game_info, _, rest = line.partition(":")  # -> ('Game #', ':', '...')
        game_id = int(game_info.split()[1])  # -> # in Game #
        valid_game = True

        # dict to hold colors for each game
        colors = {"red": 0, "green": 0, "blue": 0}

        # iterates through each game-set
        for game_set in rest.split(";"):
            cubes = game_set.split(",")

            # iterates through each cube and its color for each set
            for cube in cubes:
                cubeline = cube.strip().split()
                num = int(cubeline[0])
                color = cubeline[1].lower()
                colors[color] = num

                # invalid game if these criteria are met
                if colors["red"] > MAX_RED or colors["green"] > MAX_GREEN or colors["blue"] > MAX_BLUE:
                    valid_game = False

        # adds sum if valid game ↑
        if valid_game:
            id_sum += game_id

    return id_sum


def part_two(data):
    id_sum = 0

    for line in data:

        # Extracts the game
        _, _, rest = line.partition(":")  # -> ('Game #', ':', '...')

        # dict to hold colors for each game
        colors = {"red": 0, "green": 0, "blue": 0}

        # iterates through each game-set
        for game_set in rest.split(";"):
            cubes = game_set.split(",")

            # iterates through each cube and its color for each set
            for cube in cubes:
                cubeline = cube.strip().split()
                num = int(cubeline[0])
                color = cubeline[1].lower()

                # saves only the highest number
                if num > colors[color]:
                    colors[color] = num

        # calculates the power of the cubes
        power = colors["red"] * colors["green"] * colors["blue"]
        id_sum += power

    return id_sum


col_sum = part_one(data)
pow_sum = part_two(data)
print("part one:", col_sum)
print("part two:", pow_sum)
