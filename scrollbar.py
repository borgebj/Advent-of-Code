
inputs = [int(x) for x in input().split()]
w = inputs[0]
h = inputs[1]
f = inputs[2]
n = inputs[3]

string = ""

for x in range(n):
    line = input()
    string += line + " "

print(string)