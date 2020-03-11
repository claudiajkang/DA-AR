import sys

st = sys.stdin.readline().strip()
stack = []
prior = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for ch in '(' + st + ')':
    if ch.isupper():
        print(ch, end='')
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while True:
            o = stack.pop()
            if o == '(':
                break
            print(o, end='')
    else:
        while stack[-1] != '(' and prior[ch] <= prior[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(ch)
