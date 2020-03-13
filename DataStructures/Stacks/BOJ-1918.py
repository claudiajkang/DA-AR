from sys import stdin

ch = '(' + stdin.readline().rstrip() + ')'
stack = []
cal = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
res = ''

for c in ch:
    if c.isupper():
        res += c
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack:
            v = stack.pop()
            if v == '(':
                break
            res += v
    else:
        while stack[-1] != '(' and cal[c] <= cal[stack[-1]]:
            res += stack.pop()

        stack.append(c)

print(res)