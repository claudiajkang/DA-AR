import sys

N = int(sys.stdin.readline())

for i in range(N):
    line = sys.stdin.readline()
    s = list()

    for j in line:
        if j == '(':
            s.append(j)
        elif j == ')':
            if len(s) > 0 and s[-1] == '(':
                v = s.pop()
            else:
                s.append(j)

    if s:
        print('NO')
    else:
        print('YES')