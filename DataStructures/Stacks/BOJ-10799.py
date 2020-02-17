from sys import stdin
  
S = stdin.readline().strip()
stack = []
res = 0

for i in range(len(S)):
    if stack and (S[i-1] == '(' and S[i] == ')'):
        v = stack.pop()
        res += len(stack)
    elif stack and (stack[-1] == '(' and S[i] == ')'):
        v = stack.pop()
        res += 1
    else:
        stack.append(S[i])

print(res)
