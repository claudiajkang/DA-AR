from sys import stdin

s = stdin.readline()[:-1]
res = []

for i in s:
    if 65 <= ord(i) <= 90:
        v = ord(i) + 13
        if v > 90:
            v -= 26

        res.append(chr(v))

    elif 97 <= ord(i) <= 122:
        v = ord(i) + 13
        if v > 122:
            v -= 26

        res.append(chr(v))

    else:
        res.append(i)

print(''.join(res))
