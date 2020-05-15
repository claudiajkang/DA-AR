from sys import stdin

s = stdin.readline().rstrip()
a = {chr(97+i) : -1 for i in range(26)}

for i in range(len(s)):
    if a[s[i]] == -1:
        a[s[i]] = i

print(' '.join(map(str, a.values())), end = '')
