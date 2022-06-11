file_path = './numbers.txt'

file = open(file_path, 'r')
# или file = open('./numbers.txt', 'r')

the_sum = 0
for line in file:
    the_sum += int(line)

print(the_sum)
# или  print(sum([int(x) for x in file]))

# *********Other solution but not so used*********
# print(sum([int(x) for x in open('./numbers.txt', 'r')]))
