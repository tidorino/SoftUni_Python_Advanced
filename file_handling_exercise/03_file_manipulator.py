"""
********** InPut************

Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End

"""

from os import remove
from os.path import exists


def create_file(name):
    with open(f'./{name}', 'w') as file:
        pass
    return file


def add_to_file(name, text):
    with open(f'./{name}', 'a') as file:
        file.write(text + '\n')
    return file


def replace_in_file(name, old_text, new_text):
    with open(f'./{name}', 'r+') as file:
        file_content = file.read().replace(old_text, new_text)
        file.seek(0)
        file.truncate(0)
        file.write(file_content)
    return file


def delete_file(name):
    with open(f'./{name}', 'w') as file:
        pass
    return file


while True:
    command = input()
    if command == 'End':
        break
    command_parts = command.split('-')
    new_command, file_name = command_parts[0], command_parts[1]

    if new_command == 'Create':
        result = create_file(file_name)
    elif new_command == 'Add':
        content = command_parts[2]
        result = add_to_file(file_name, content)
    elif new_command == 'Replace':
        if not exists(f'./{file_name}'):
            print(f'An error occurred')
            continue

        old_string, new_string = command_parts[2],  command_parts[3]
        result = replace_in_file(file_name, old_string, new_string)
    elif new_command == 'Delete':
        if not exists(f'./{file_name}'):
            print(f'An error occurred')
            continue
        else:
            remove(file_name)
