# ребуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

list_1 = [1, 2, 3, 4, 5]
k = 3
res = 0
for elem in list_1:
    if elem == k:
        res += 1

print(res)