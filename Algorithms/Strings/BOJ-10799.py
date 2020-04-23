from sys import stdin

strings = stdin.readline().rstrip()
stack = []
res = 0

for i in range(len(strings)):
    if stack and strings[i - 1] == '(' and strings[i] == ')':
        stack.pop()
        res += len(stack)

    elif stack and stack[-1] == '(' and strings[i] == ')':
        stack.pop()
        res += 1

    else:
        stack.append(strings[i])

print(res)