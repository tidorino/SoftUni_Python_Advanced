numb = [int(n) for n in input().split()]

n = {int(input()) for _ in range(numb[0])}
m = {int(input()) for _ in range(numb[1])}

[print(number) for number in n.intersection(m)]

