"""
On the first line, you will receive the number of commands - N.
On the following N lines, you will receive the direction and car's number
in the format: "{direction}, {car_number}".
The direction could only be "IN" or "OUT".
Print the car numbers which are still in the parking lot
"""


number_parking_cars = int(input())

parking_set = set()

for _ in range(number_parking_cars):
    parking_info, car_number = input().split(", ")

    # **** other solution ******
# parking_lot_logs = [input().split(", ") for _ in range(number_parking_cars)]
# for parking_info, car_number in parking_lot_logs:

    if parking_info == "IN":
        parking_set.add(car_number)

    else:
        parking_set.remove(car_number)

if parking_set:
    [print(car) for car in parking_set]
else:
    print('Parking Lot is Empty')

