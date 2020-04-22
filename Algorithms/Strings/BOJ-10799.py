from sys import stdin

s = stdin.readline().rstrip()
stack = []
res = 0

for i in range(len(s)):
    if stack and s[i-1] == '(' and s[i] == ')':
        v = stack.pop()
        res += len(stack)

    elif stack and stack[-1] == '(' and s[i] == ')':
        v = stack.pop()
        res += 1

    else:
        stack.append(s[i])

print(res)