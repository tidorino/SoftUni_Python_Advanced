"""
You will be given a sequence consisting of parentheses.
Your job is to determine whether the expression is balanced.
A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis
that occurs after the former. There will be no interval symbols between the parentheses.
You will be given three types of parentheses: (), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
"""

expression = input()

stack_opening_brackets = []
pair_brackets = {'{': '}', '[': ']', '(': ')'}
balance = True

for i in expression:

    if i in '{[(':
        stack_opening_brackets.append(i)

    elif not stack_opening_brackets:
        balance = False

    else:
        last_opening_brackets = stack_opening_brackets.pop()
        if pair_brackets[last_opening_brackets] != i:
            balance = False

    if not balance:
        break


if not balance or stack_opening_brackets:
    print("NO")
else:
    print("YES")



