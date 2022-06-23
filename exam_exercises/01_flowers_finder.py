"""
You will be given two sequences of characters,
representing vowels and consonants. Your task is to start checking if the following words could be found.

Input:
o e a o e a i
p r s x r

"""

from collections import deque

vowels = deque(input().split())
consonants = input().split()

word_dict = {
    'rose': 'rose',
    'tulip': 'tulip',
    'lotus': 'lotus',
    'daffodil': 'daffodil',
}
word_found = []
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for key in word_dict.keys():
        if vowel in key:
            word_dict[key] = word_dict[key].replace(vowel, '')
        if consonant in key:
            word_dict[key] = word_dict[key].replace(consonant, '')

        if word_dict[key] == '':
            word_found.append(key)
            break
    if word_found:
        break

if word_found:
    print(f'Word found: {"".join(word_found)}')
else:
    print(f'Cannot find any word!')
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")



