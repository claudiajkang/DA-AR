from sys import stdin

for j in stdin:
    res = [0] * 4

    for i in j:
        if i.isupper():
            res[1] += 1

        elif i.islower():
            res[0] += 1

        elif i == ' ':
            res[3] += 1

        elif i.isdigit():
            res[2] += 1

        elif i == '\n':
            break

    print(' '.join(map(str, res)))