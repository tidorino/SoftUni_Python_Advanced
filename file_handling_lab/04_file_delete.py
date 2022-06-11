from os import remove
from os.path import exists

# file_path = open('../file_handling_lab/deleted_text.txt', 'w')
file = './deleted_text.txt'
if exists(file):
    remove(file)
    print('File deleted')
else:
    print('File already deleted')


