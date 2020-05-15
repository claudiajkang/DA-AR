from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())

for i in range(n):
    stack = []

    arr = read()

    for j in arr:
        if stack and j == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(j)

    if stack:
        print("NO")

    else:
        print("YES")
