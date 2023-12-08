
cats = {0:"seed-to-soil", 1:"soil-to-fertilizer", 2:"fertilizer-to-water", 3:"water-to-light",
        4:"light-to-temperature", 5:"temperature-to-humidity", 6:"humidity-to-location" }

with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

# parsing data into their own "categories"
# seeds are ints in a list
seeds = [int(n) for n in lines[0].split(":")[1].split()]
# maps are  lists of lists for each category
maps = [[[int(m) for m in n.split()] for n in l.split(":\n")[1].splitlines()] for l in lines[1:]]

ranges = [[]for _ in range(len(cats))]
print(ranges)
for i, m in enumerate(maps):
    print(i, "-", cats[i])
    for d, s, l in m:
        print("d", d, "s", s, "l", l)
        ranges[i].append([s, s+l, d])
    print()

print(ranges)