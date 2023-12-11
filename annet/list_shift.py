
list = [1, 2, 3, 4]
olist = list.copy()
n = len(list)


for i in range(n - 1):
    print("i =", i)
    for j in range(i, n - 1):
        list[j], list[j+1] = list[j+1], list[j]
        print(f'{list} {list[j+1]} og {list[j]} - {j} og {j+1}')
    print()

print(f'Original   {olist}')
print(f'End result {list}')

# shifts elements forward from first to last index
# 0->1->2->3
# 1->2->3
# 2->3
# 3

# i=0
# [1,2,3,4]
# [2,1,3,4] 1 og 2 - 0 og 1
# [2,3,1,4] 1 og 3 - 1 og 2
# [2,3,4,1] 1 og 4 - 2 og 3

# i=1
# [2,3,4,1]
# [2,4,3,1] 3 og 4 - 1 og 2
# [2,4,1,3] 3 og 1 - 2 og 3

# i=2
# [2,4,1,3]
# [2,4,3,1] 1 og 3 - 2 og 3
