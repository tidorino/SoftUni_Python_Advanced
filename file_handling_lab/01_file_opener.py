file_path = './text.txt'
file = open(file_path, 'r')
try:
    open(file_path, 'r')
    print('File found')
    while True:
        line = file.readline()
        if not line:
            break
        print(line, end='')

except FileNotFoundError:
    print('File not found')
