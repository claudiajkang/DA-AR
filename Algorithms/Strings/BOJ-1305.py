from sys import stdin
read = lambda: stdin.readline().rstrip()

l = int(read())
s = read()

fail = [0] * l

j = 0
for i in range(1, l):
    if j > 0 and s[i] != s[j]:
        j = fail[j - 1]

    if s[i] == s[j]:
        j += 1
        fail[i] = j

print(l - fail[-1])
