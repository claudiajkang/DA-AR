from sys import stdin

next(stdin)
for line in stdin:
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