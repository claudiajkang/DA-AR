from sys import stdin

s = stdin.readline().rstrip()
res = ''

for i in s:
    if i.isupper():
        idx = ord(i) + 13 if (ord(i) + 13) <= 90 else ord(i) + 13 - 26
        res += chr(idx)

    elif i.islower():
        idx = ord(i) + 13 if (ord(i) + 13) <= 122 else ord(i) + 13 - 26
        res += chr(idx)

    else:
        res += i

print(res)