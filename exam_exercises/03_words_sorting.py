def words_sorting(*args):
    words_dict = {}
    for i in range(len(args)):
        word = args[i]
        value = sum(ord(chr) for chr in word)
        if word in words_dict:
            words_dict[word] += value
        else:
            words_dict[word] = value
    sum1 = sum(words_dict.values())

    if sum1 % 2 != 0:
        result = sorted(words_dict.items(), key=lambda x: -x[1])

    else:
        result = sorted(words_dict.items(), key=lambda x: x[0])

    sorted_w = [f'{key} - {value}' for key, value in result]
    return '\n'.join(sorted_w)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

