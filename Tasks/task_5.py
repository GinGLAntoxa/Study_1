"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
"""
def find_closest_element(arr, k):
    closest = None
    min_diff = float('inf')
    for num in arr:
        diff = num - k
        if diff < 0:
            diff = -diff
        if diff < min_diff:
            min_diff = diff
            closest = num
    return closest

list_1 = [22, 5, 9, 12, 17]
k = 3

result = find_closest_element(list_1, k)
print(result)

# 2 решения через abs

m = abs(k - list_1[0])
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(m)