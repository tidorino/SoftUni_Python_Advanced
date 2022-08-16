from collections import deque


def get_present_result(gift_sum, material, magic):
    if gift_sum < 100 and gift_sum % 2 == 0:
        gift_sum = material * 2 + magic * 3
        return gift_sum
    elif gift_sum < 100 and gift_sum % 2 != 0:
        gift_sum *= 2
        return gift_sum
    elif gift_sum > 499:
        gift_sum /= 2
        return gift_sum
    else:
        return gift_sum


def add_gift(gift, gifts):
    gifts[gift] += 1
    return gifts


def if_in_table(present_result):
    if 100 <= present_result <= 199:
        return 'Gemstone'
    elif 200 <= present_result <= 299:
        return 'Porcelain Sculpture'
    elif 300 <= present_result <= 399:
        return 'Gold'
    elif 400 <= present_result <= 499:
        return 'Diamond Jewellery'


materials = [int(x) for x in input().split(' ')]
magic_level = deque(int(x) for x in input().split(' '))

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    present_sum = material + magic

    present_result = get_present_result(present_sum, material, magic)
    if present_result < 100 or present_result > 499:
        continue
    gift = if_in_table(present_result)
    gifts = add_gift(gift, gifts)

if gifts['Gemstone'] and gifts['Porcelain Sculpture'] or gifts['Gold'] and gifts['Diamond Jewellery']:
    print('The wedding presents are made!')

else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f"Materials left: {', '.join([str(m) for m in materials])}")

if magic_level:
    print(f"Magic left: {', '.join([str(m) for m in magic_level])}")

for key, value in sorted(gifts.items()):
    if value:
        print(f"{key}: {value}")
