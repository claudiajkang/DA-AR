import sys

w = sys.stdin.readline().replace('\n', '')

alpa = 'abcdefghijklmnopqrstuvwxyz'
r = dict()

for i in alpa:
    r[i] = -1

for j in range(len(w)):
    k = w[j]
    if r[k] == -1:
        r[k] = j

for i in alpa:
    print(r[i], end = ' ')
