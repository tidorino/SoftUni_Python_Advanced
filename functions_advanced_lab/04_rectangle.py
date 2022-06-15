def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * length + 2 * width

    if not isinstance(length, int) or not isinstance(width, int):
        return f'Enter valid values!'

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'


print(rectangle(2, 10))
print(rectangle('2', 10))
