from sys import stdin

s = stdin.readline().rstrip()
res = {chr(97+i): 0 for i in range(26)}

for i in s:
    res[i] += 1

print(' '.join(map(str, res.values())))
