with open("input.txt", "r") as f:
    data = [[int(x) for x in line.split()] for line in f]
# parsing


# finds history sum iteratively
def history_sum_it(data: list) -> int:
    history_sum = 0
    for line in data:
        last_values = []

        # continues until line is zero: [0, 0, ..., 0]
        while any(line):
            print(*line)
            last_values.append(line[-1])  # saves last number
            line = [next_e - curr_e for curr_e, next_e in zip(line, line[1:])]  # turns line into differences-list

        history_sum += sum(reversed(last_values))
        print()

    return history_sum  # total sum of last values returned


# finds history sum recursively
def history_sum_rec_in(data: list) -> int:
    def history_sum_rec(differences: list, last_values) -> int:

        # base case: stops at "zero list": [0, 0, ..., 0]
        if all(x == 0 for x in differences):
            return sum(last_values)

        # calculates differences between current and next in new list
        last_values.insert(0, differences[-1])
        differences = [next_e - curr_e for curr_e, next_e in zip(differences, differences[1:])]
        return history_sum_rec(differences, last_values)

    return sum(history_sum_rec(line, []) for line in data)


his_sum = history_sum_it(data)
# his_sum = history_sum_rec_in(data)
print(f'Sum of extrapolated history sum is {format(his_sum, ",")}')
