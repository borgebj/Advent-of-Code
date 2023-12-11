from functools import reduce

# parsing
with open("input.txt", "r") as f:
    data = [[int(x) for x in line.split()] for line in f]


# finds history sum iteratively
# difference-list creations happens in the while-loop
# calculating sums happens after the while-loop
def history_sum_it(data: list) -> (int, int):
    future_history_sum = 0
    past_history_sum = 0
    for line in data:
        last_values = []
        first_values = []

        # continues until line is zero: [0, 0, ..., 0]
        while any(line):
            last_values.append(line[-1])  # saves last number
            first_values.append(line[0])  # saves first number
            line = [next_e - curr_e for curr_e, next_e in zip(line, line[1:])]  # turns line into differences-list

        # part 1: calculates and stores cumulative sum of all last-values
        future_history_sum += sum(reversed(last_values))

        # part 2: calculates and stores reversed cumulative sum of all first-values
        past_history_sum += reduce(lambda x, y: y - x, reversed(first_values))

    return past_history_sum, future_history_sum  # total sum of last values returned


# finds history sum recursively
# difference-list creation happens in the recursion-function
# calculating sums happens in the initiation-function
def history_sum_rec_in(data: list) -> (int, int):
    def history_sum_rec(differences: list, last_values: list, first_values: list) -> (int, int):

        # base case: stops at "zero list": [0, 0, ..., 0]
        if all(x == 0 for x in differences):
            return reduce(lambda x, y: y - x, reversed(first_values)), sum(last_values)

        # calculates differences between current and next in new list
        last_values.append(differences[-1])  # saves last number
        first_values.append(differences[0])  # saves first number
        differences = [next_e - curr_e for curr_e, next_e in zip(differences, differences[1:])]
        return history_sum_rec(differences, last_values, first_values)

    # Extracts both past and future values in pairs
    vals = [(past, future) for past, future in [history_sum_rec(line, [], []) for line in data]]
    past_vals, future_vals = zip(*vals)
    return sum(past_vals), sum(future_vals)


past_sum, future_sum = history_sum_it(data)
print(f'Rec: Sum of extrapolated past and future history sum is {format(past_sum, ",")} and {format(future_sum, ",")}')
past_sum, future_sum = history_sum_rec_in(data)
print(f'it: Sum of extrapolated past and future history sum is {format(past_sum, ",")} and {format(future_sum, ",")}')


# notes part 2
"""
    start_tall = [10, 3, 0, 2]
    omvendt = [2, 0, 3, 10]
    
    4 elementer, 4 iterasjoner
    
    ** itererer gjennom omvendt med curr start på 0 (siden siste diff-liste er bare 0) **

    it. 1
    (prev) - (curr) = (new)  -->  2 - 0 = 2
    curr = new  -->  (0 = 2)
    
    it. 2
    (prev) - (curr) = (new)  -->  0 - 2 = (-2) 
    curr = new  -->  (2 = -2)
    
    it. 3
    (prev) - (curr) = (new)  -->  3 - (-2) = 5
    curr = new  -->  (-2 = 5)
    
    it. 4
    (prev) - (curr) = (new)  -->  10 - 5 = 5 
    curr = new  -->  (-5 = 5) 
    
    basic kode med denne ideen:
        curr = 0
        for x in reversed(first_values):
            new = x - curr
            curr = new
"""