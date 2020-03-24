from sys import stdin
read = lambda: int(stdin.readline().rstrip())

stack = []
n = read()
arr = [read() for i in range(n)]
r = []

for i in range(1, n+1):
    stack.append(i)
    r.append('+')

    while stack and stack[-1] == arr[0]:
        stack.pop()
        r.append('-')
        arr.pop(0)

if not stack:
    print('\n'.join(r))

else:
    print('NO')