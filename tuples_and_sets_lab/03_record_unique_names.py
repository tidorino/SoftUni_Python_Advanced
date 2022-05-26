number_names = int(input())
name_set = set()

for _ in range(number_names):
    name = input()
    name_set.add(name)

# for n in name_set:
#     print(f'{n}')

[print(n) for n in name_set]

# ***** Other solution *****:

# n = int(input())
# name_set = {input() for _ in range(n)}
# [print(name) for name in name_set]
