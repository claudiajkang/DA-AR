from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
st = read()
val = {chr(65+i): int(read()) for i in range(n)}
stack = []

for i in st:
    if i.isupper():
        stack.append(val[i])
    else:
        v = []
        for j in range(2):
            a = stack.pop()
            v.append(a)

        if i == '+': stack.append(v[1] + v[0])
        elif i == '-': stack.append(v[1] - v[0])
        elif i == '/': stack.append(v[1] / v[0])
        elif i == '*': stack.append(v[1] * v[0])

print('%.2f' % stack.pop())
