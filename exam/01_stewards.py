from collections import deque

seats = input().split(', ')
first_numbers = deque(int(x) for x in input().split(', '))
second_numbers = deque(int(x) for x in input().split(', '))

matched_seats = []
rotation_counter = 0
match = True


def find_seat(n1, n2):
    sum_of_both_numb = n1 + n2
    ascii_letter = chr(sum_of_both_numb)

    numb1 = f'{n1}'+f'{ascii_letter}'
    numb2 = f'{n2}'+f'{ascii_letter}'
    return numb1, numb2


while True:
    match = True
    if len(matched_seats) == 3:
        break
    if rotation_counter == 10:
        break

    first = first_numbers.popleft()
    second = second_numbers.pop()
    looking_seat1, looking_seat2 = find_seat(first, second)
    rotation_counter += 1

    for seat in seats:
        if seat == looking_seat1:
            # if seat in matched_seats:
            #     continue
            if seat not in matched_seats:

                matched_seats.append(seat)
                match = False
        elif seat == looking_seat2:
            matched_seats.append(seat)
            match = False
    if match:
        first_numbers.append(first)
        second_numbers.appendleft(second)

if len(matched_seats) == 3 or rotation_counter == 10:
    print(f'Seat matches: {", ".join(x for x in matched_seats)}\nRotations count: {rotation_counter}')
