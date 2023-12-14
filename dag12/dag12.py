# parsing
with open("input.txt", "r") as f:
    data = [[x for x in line.split()] for line in f]


for line in data:
    springs = line[0]
    known = line[1]
