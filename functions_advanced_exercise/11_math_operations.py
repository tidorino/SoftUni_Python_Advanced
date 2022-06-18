def math_operations(*args, **kwargs):

    for key, value in kwargs.items():
        if key == 'a':
            for el in range(0, len(args), 4):
                kwargs[key] += args[el]
        elif key == 's':
            for el in range(1, len(args), 4):
                kwargs[key] -= args[el]
        elif key == 'd':
            for el in range(2, len(args), 4):
                try:
                    kwargs[key] /= args[el]
                except ZeroDivisionError:
                    continue
        elif key == 'm':
            for el in range(3, len(args), 4):
                kwargs[key] *= args[el]
    sorted_values = [f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(),key=lambda x: (-x[1], x[0]))]
    return '\n'.join(sorted_values)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
