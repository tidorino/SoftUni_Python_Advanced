number = int(input())

odd_set = set()
even_set = set()
current_row = 1
for row in range(1, number + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

even_sum = sum(even_set)
odd_sum = sum(odd_set)
if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(*result, sep=', ')
