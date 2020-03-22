from sys import stdin
read = lambda: stdin.readline().rstrip()

stack = []
n = int(read())
exp = read()
val = {chr(65+i): int(read()) for i in range(n)}

for i in exp:
    if i.isupper():
        stack.append(val[i])

    elif i in '*+/-':
        b = stack.pop()
        a = stack.pop()

        if i == '*':
            stack.append(a*b)

        elif i == '/':
            stack.append(a/b)

        elif i == '+':
            stack.append(a+b)

        elif i == '-':
            stack.append(a-b)

print("%.2f" % (stack.pop()))
