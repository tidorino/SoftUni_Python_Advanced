"""
Write a program that reads a text
from the console and counts the occurrences of each character in it.
Print the results in alphabetical (lexicographical) order.

"""
string = input()
new_str = tuple(sorted(string))

dict_char = {}

for i in new_str:
    if i not in dict_char:
        dict_char[i] = 0

    dict_char[i] += 1

for char, count in dict_char.items():
    print(f"{char}: {count} time/s")



