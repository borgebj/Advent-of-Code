# parsing
with open("input", "r") as f:
    data = [list(word) for word in f.read().split(",")]


def hash(inp, total=0):
    for row in inp:
        current_value = 0
        for elem in row:
            current_value += ord(elem)  # increase current by ASCII code
            current_value *= 17         # multiply itself by 17
            current_value %= 256        # rest from self modulo 256

        total += current_value
    return total


pos = hash(data)

# part 1
print(f'Sum of results from hashing: {pos}')

# Find ASCII
# Increase the current value by ASCII
# Set the current value to self * 17
# Set the current value to self % 256
