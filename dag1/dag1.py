
# borgebj
# part of Advent of code 2023 day 1
# https://adventofcode.com/2023/day/1#part2


# part 1
# only numbers
def main1(input):
    """Goes through file and finds the total sum of the number from the first and last digit of each line
    Includes only digits like 1,2,3, etc.

    param:
        input (string): name of input-file
    return:
        int: total sum
    """
    inp = open(input)
    sum = 0

    # iterates through lines saving first and last number
    for line in inp:
        first = ""
        last = ""

        # checks for numbers
        for letter in line:

            # first is assigned once, last gets overwritten
            if letter.isdigit():
                if not first:
                    first = letter
                last = letter


        # adds combined numbers to total
        sum += int(first+last)

    # returns total
    return sum

# print( main1("input.txt") )


# part 2
# including words to number
words = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def main2(input):
    """Goes through file and finds the total sum of the number from the first and last digit of each line
    Includes both digits like 1,2,3, etc. AND worded numbers like "one", "two", "three", etc.

    param:
        input (string): name of input-file
    return:
        int: total sum
    """
    inp = open(input)
    sum = 0

    for line in inp:
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
        sum += int(first+last)

    # returns total
    return sum

print( main2("input.txt") )

