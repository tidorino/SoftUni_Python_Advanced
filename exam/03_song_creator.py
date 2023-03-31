import os


def add_songs(*args):
    add_songs_dict = {}
    for items in args:
        song_title = items[0]
        list_of_lyrics = items[1]

        if song_title not in add_songs_dict:
            add_songs_dict[song_title] = []
        if len(list_of_lyrics) == 0:
            continue
        if list_of_lyrics:
            for item in list_of_lyrics:
                add_songs_dict[song_title] += [item]

    result = ''
    for song, lyric in add_songs_dict.items():
        result += f'- {song}\n'
        if len(lyric) == 0:
            continue
        result += f'{os.linesep.join(lyric)}\n'
    return result.strip()


# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))

# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))