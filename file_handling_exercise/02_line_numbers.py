import string

with open('./text.txt', 'r') as file, open('./output.txt', 'w') as result:
    for idx, line in enumerate(file):
        letters_count = 0
        punctuation_count = 0

        for row in line.split():
            for symbol in row:
                if symbol in string.ascii_letters:
                    letters_count += 1
                if symbol in string.punctuation:
                    punctuation_count += 1

        result.write(f'Line {idx + 1}: {line.strip()} ({letters_count})({punctuation_count})\n')
