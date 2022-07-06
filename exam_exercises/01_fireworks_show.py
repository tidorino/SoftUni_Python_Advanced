from collections import deque

fireworks_effects = deque(int(x) for x in input().split(','))
explosive_power = [int(x) for x in input().split(',')]

willow_firework = 0
palm_firework = 0
crossette_fireworks = 0
while fireworks_effects and explosive_power:
    firework = fireworks_effects.popleft()
    explosive = explosive_power.pop()
    if firework <= 0:
        explosive_power.append(explosive)
        continue
    elif explosive <= 0:
        fireworks_effects.appendleft(firework)
        continue

    sum_items = firework + explosive
    if sum_items % 3 == 0 and sum_items % 5 == 0:
        crossette_fireworks += 1
    elif sum_items % 3 == 0 and sum_items % 5 != 0:
        palm_firework += 1
    elif sum_items % 3 != 0 and sum_items % 5 == 0:
        willow_firework += 1
    else:
        firework -= 1
        fireworks_effects.append(firework)
        explosive_power.append(explosive)

    if willow_firework >= 3 and palm_firework >= 3 and crossette_fireworks >= 3:
        break

if willow_firework >= 3 and palm_firework >= 3 and crossette_fireworks >= 3:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    result = ", ".join(str(x) for x in fireworks_effects)
    print(f'Firework Effects left: {result}')
if explosive_power:
    result = ", ".join(str(x) for x in explosive_power)
    print(f'Explosive Power left: {result}')

print(f'Palm Fireworks: {palm_firework}')
print(f'Willow Fireworks: {willow_firework}')
print(f'Crossette Fireworks: {crossette_fireworks}')

