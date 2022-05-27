"""
On the first line you will be given a number n - the count of input lines
that you are going to receive. On the next n lines, you will be receiving chemical compounds,
separated by a single space.Your task is to print all the unique ones.
3
Ge Ch O Ne
Nb Mo Tc
O Ne

"""

n = int(input())

chemical_elements = set()
for _ in range(n):
    item = input().split()

    for i in item:
        chemical_elements.add(i)

[print(element) for element in chemical_elements]

# ******** other solution:
# current_set = set(input().split())
# result = result.union(current_set)
# for el in result:
# print(el)
# *************



