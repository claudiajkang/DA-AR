from sys import stdin
read = lambda: int(stdin.readline().rstrip())

n = read()
stack = []
arr = [read() for i in range(n)]
res = ""

for i in range(1, n+2):
    while stack and stack[-1] == arr[0]:
        stack.pop()
        arr.pop(0)
        res += '-\n'

    if i == n+1:
        break
    stack.append(i)
    res += '+\n'

print('NO' if stack else res)