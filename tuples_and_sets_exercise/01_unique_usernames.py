numbs_usernames = int(input())

# ****************
# username = set()
# for _ in range(numbs_usernames):
#     username.add(input())
# *******************
username = {input() for _ in range(numbs_usernames)}
[print(name) for name in username]
