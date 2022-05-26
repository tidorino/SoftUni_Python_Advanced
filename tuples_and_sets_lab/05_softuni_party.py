n = int(input())

regular_guests = set()
vip_guests = set()

for _ in range(n):
    code = input()
    if code[0].isdigit():
        vip_guests.add(code)

    else:
        regular_guests.add(code)

while True:
    command = input()
    if command == 'END':
        break

    if command in vip_guests:
        vip_guests.remove(command)
    elif command in regular_guests:
        regular_guests.remove(command)
# ***** too slow in judge *****
# one_list = [guest_not_come for guest_not_come in vip_guests.union(regular_guests)]

# print(f'{len(one_list)}')
# [print(''.join(codes)) for codes in sorted(one_list)]

print(len(vip_guests) + len(regular_guests))
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]
