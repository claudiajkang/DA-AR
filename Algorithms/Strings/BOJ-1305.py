from sys import stdin

read = lambda: stdin.readline().rstrip()

l = int(read())
p = read()

fail = [0] * l

j = 0

for i in range(1, l):
    if j > 0 and p[i] != p[j]:
        j = fail[j - 1]

    if p[i] == p[j]:
        j += 1
        fail[i] = j

print(l - fail[-1])
