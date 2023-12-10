# borgebj
# part of Advent of code 2023 day 1
# https://adventofcode.com/2023/day/1#part2

with open("input.txt") as f:
    data = f.read().splitlines()


# part 1
# only numbers
def part_one(data: list[str]) -> int:
    total_sum = 0

    # iterates through lines saving first and last number
    for line in data:
        digits = [char for char in line if char.isdigit()]

        if digits:
            total_sum += int(digits[0] + digits[-1])  # adds first and last

    # returns total
    return total_sum


# part 2
# including words to number
words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
         "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def part_two(data):
    sum = 0

    # iterates through lines saving first and last number
    for line in data:
        first = ""
        last = ""

        # iterates through each letter in a line to find digits or worded-numbers
        for i in range(len(line)):
            if line[i].isdigit():
                if not first:
                    first = line[i]
                last = line[i]

            else:
                # creates substrings using the following letters after current letter
                for j in range(i + 1, len(line) + 1):
                    sub = line[i:j]
                    if sub in words:
                        if not first:
                            first = words[sub]
                        last = words[sub]

        # adds combined numbers to total
        sum += int(first + last)

    # returns total
    return sum


tot_sum = part_one(data)
num_sum = part_two(data)
print("Part one:", tot_sum)
print("Part two:", num_sum)


# super-short regex
import re

# part 1
nums = [num for line in data for num in [re.findall(r"[0-9]", line)]] # detects digits 0-9
print(f'Part one R: {sum(int(num[0] + num[-1]) for num in nums if num)}')

# part 2
nums = [num for line in data for num in [re.findall(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)]] # detects both text and digit
print(f'Part two R: {sum([int(words.get(num[0], num[0]) + words.get(num[-1], num[-1])) for num in nums])}')

