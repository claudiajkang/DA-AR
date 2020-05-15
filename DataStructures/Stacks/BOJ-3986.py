from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
word = [read() for i in range(n)]
res = 0

for i in range(n):
    stack = []
    
    for w in word[i]:
        if stack and stack[-1] == w:
            while stack and stack[-1] == w:
                stack.pop()
        else:
            stack.append(w)

    if not stack:
        res += 1

print(res)
