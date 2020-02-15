import sys

a = 'abcdefghijklmnopqrstuvwxyz'
B = a.upper()
v = ['lo', 'up', 'di', 'bl']

for line in sys.stdin:
    res = dict()

    for k in v:
        res[k] = 0

    for i in line:
        if i in a:
            res['lo'] += 1
        elif i in B:
            res['up'] += 1
        elif i == ' ':
            res['bl'] += 1
        elif i == '\n':
            continue
        else:
            res['di'] += 1

    for k in v:
        print(res[k], end = ' ')
