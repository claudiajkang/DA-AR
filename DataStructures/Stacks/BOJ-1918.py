from sys import stdin

v = '('+stdin.readline().rstrip()+')'
cal = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
stack = []

for i in v:
    if i.isupper():
        print(i, end='')

    elif i == '(':
        stack.append(i)

    elif i == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()

    elif i in cal.keys():
        while stack[-1] != '(' and cal[i] <= cal[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(i)


