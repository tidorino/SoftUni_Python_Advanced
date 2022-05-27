"""
You will be given a number N.
On each of the next N lines you will be given two ranges in
the format: "{first_start},{first_end}-{second_start},{second_end}".
You should find the longest intersection of all N intersections.
"""


def intersection(number):
    first_start, first_end = [int(x) for x in number[0].split(',')]
    second_start, second_end = [int(x) for x in number[1].split(',')]
    first_intersection = set(range(first_start, first_end + 1))
    second_intersection = set(range(second_start, second_end + 1))
    return first_intersection.intersection(second_intersection)


numb = int(input())
longest_intersection = set()

for _ in range(numb):
    # number_ranges =
    info_intersection = intersection(input().split('-'))
    if len(info_intersection) > len(longest_intersection):
        longest_intersection = info_intersection

print(f'Longest intersection is [{", ".join([str(x) for x in longest_intersection])}] with length'
      f' {len(longest_intersection)}')
