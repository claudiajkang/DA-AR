from sys import stdin

s = stdin.readline().replace('\n','')
stack = list()
res = 0

for i in range(len(s)):
    if not stack:
        stack.append(s[i])
        continue

    if s[i-1] == '(' and s[i] == ')':
        v = stack.pop()
        res += len(stack)
    elif s[i] == ')' and stack[-1] == '(':
        v = stack.pop()
        res += 1
    else:
        stack.append(s[i])

print(res)
