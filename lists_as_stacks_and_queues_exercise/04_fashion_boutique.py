clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_counter = 1
current_rack_capacity = rack_capacity

while clothes_stack:

    current_cloth = clothes_stack.pop()
    if current_cloth > current_rack_capacity:
        racks_counter += 1
        current_rack_capacity = rack_capacity
        current_rack_capacity -= current_cloth
    else:
        current_rack_capacity -= current_cloth

print(racks_counter)



