def positiv_negtiv_sum(*args):
    positive_sum = 0
    negative_sum = 0
    for numb in args:
        if numb < 0:
            negative_sum += numb
        else:
            positive_sum += numb
    return positive_sum, negative_sum


numbers = [int(x) for x in input().split()]
positive_sum, negative_sum = positiv_negtiv_sum(*numbers)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')
