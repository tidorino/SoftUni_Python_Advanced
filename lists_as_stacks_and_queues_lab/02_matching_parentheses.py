'''
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

'1' not a bracket
' ' not a bracket
'+' not a bracket
' ' not a bracket
'(' is opening bracket
    -> add its index to the stack
'2' not a bracket
...
'(' is opening bracket
    -> add its index to the stack
'2' not a bracket
...
')' is closing bracket
    -> pop the top from the stack
    -> subexpression is between top of stack and this closing bracket
    -> index 9 , index 15 => (2 + 3)
...
'''

expression = input()

s = []

for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        s.append(i)

    elif ch == ')':
        first_index = s.pop()
        last_index = i + 1

        print(expression[first_index:last_index])

