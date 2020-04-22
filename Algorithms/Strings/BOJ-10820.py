from sys import stdin

for s in stdin:
    s = s[:-1]
    res = [0, 0, 0, 0]

    for i in s:
        if i.isupper():
            res[1] += 1
        elif i.islower():
            res[0] += 1
        elif i.isdigit():
            res[2] += 1
        else:
            res[3] += 1

    print(' '.join(map(str, res)))
