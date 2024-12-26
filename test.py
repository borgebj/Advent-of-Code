lines = int(input())

moves = 0

last = []
for x in range(lines):
    dir = input()

    lst = list(dir)

    if x == 1:
        if "V" in lst or "H" in lst:
            break

    if dir not in last:
        if len(lst) > 1:
            moves += 2
        else:
            moves += 1

    elif dir in last:
        moves -= 1

    last = lst

print(moves)

