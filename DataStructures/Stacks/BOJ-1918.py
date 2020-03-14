from sys import stdin

arr = '(' + stdin.readline().rstrip() + ')'
cal = {'(': 0, '+': 1, '-': 1, '/': 2, '*': 2}
stack = []
res = ''

for i in arr:
    if i.isupper():
        res += i

    elif i == '(':
        stack.append(i)

    elif i == ')':
        while stack:
            v = stack.pop()
            if v == '(':
                break
            res += v

    else:
        while stack[-1] != '(' and cal[i] <= cal[stack[-1]]:
            res += stack.pop()

        stack.append(i)

print(res)
