from sys import stdin

next(stdin)

for line in stdin:
        line = line.replace('\n','')
        s = list()

        for i in line:
                if s and i == ')' and s[-1] == '(':
                        v = s.pop()
                else:
                        s.append(i)

        if s:
                print('NO')
        else:
                print('YES')
