# better solutions:
# original_string[::-1]
# original_string.reverse()

original_string = input()

s = []

for c in original_string:
    s.append(c)   # push into the stack

reversed_string = ""

while s:
    reversed_string += s.pop()    # pop the top element

print(reversed_string)
