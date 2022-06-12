from os import listdir
from os.path import isdir, join


def directory_traversal(path, file_by_extension):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), file_by_extension)
        else:
            extension = element.split('.')[-1]
            if extension not in file_by_extension:
                file_by_extension[extension] = []
            file_by_extension[extension].append(element)


result = {}
directory_traversal('./', result)
final_file = open('./report.txt', 'w+')

for key, value in result.items():
    final_file.write(f'.{key}\n')
    [final_file.write(f'- - - {x}\n') for x in value]
