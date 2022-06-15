def operate(operation, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(x, *args):
        result = x
        for num in args:
            result /= num
        return result

    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

print(operate("-", 1, 2, 3))
print(operate("/", 3, 4, 2, 3))
