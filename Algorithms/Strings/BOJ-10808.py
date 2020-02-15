import sys

w = sys.stdin.readline().replace('\n','')

alpa = 'abcdefghijklmnopqrstuvwxyz'

r = dict()

for i in alpa:
    r[i] = 0

for j in w:
    r[j] += 1

for i in alpa:
    print(r[i], end =' ')
