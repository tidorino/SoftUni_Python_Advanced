def naughty_or_nice_list(kids, *args, **kwargs):
    santa_dict = {}
    kiddo = []
    for parts in args:
        n, key_word = parts.split('-')
        n = int(n)

        for numb, name in kids:
            if key_word not in santa_dict.keys():
                santa_dict[key_word] = []
            if numb == n:
                kiddo.append((numb, name))

        if len(kiddo) > 1:
            kiddo.clear()
        elif len(kiddo) == 1:
            if key_word not in santa_dict.keys():
                santa_dict[key_word] = []
            santa_dict[key_word] += [x for y, x in kiddo]
            for (item) in kiddo:
                kids.remove(item)
            kiddo.clear()

    for key, value in kwargs.items():
        for numb, name in kids:
            if name == key:
                kiddo.append((numb, name))

        if len(kiddo) > 1:
            kiddo.clear()
        else:
            santa_dict[value] += [x for y, x in kiddo]
            for (item) in kiddo:
                kids.remove(item)
            kiddo.clear()
    if kids:
        santa_dict['Not found'] = [x for y, x in kids]

    for k in santa_dict:
        if santa_dict[k]:
            print(f"{k}: {', '.join(santa_dict[k])}")
    return ''

#
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
#
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

