numbers_string = input().split(" ")

dict = {}
numbers = [float(x) for x in numbers_string]
for number in numbers:
    if number not in dict:
        dict[number] = 0

    dict[number] += 1

for number, count in dict.items():
    print(f"{number} - {count} times")

