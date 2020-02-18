from sys import stdin

N = int(stdin.readline())
TN = list(map(int, stdin.readline().strip().split()))
UN = [i for i in range(1001)]

for i in range(2, 1001):
    Q = 1000 // i
    for j in range(2, Q):
        UN[i*j] = 0

UN = sorted(UN)
z = UN.index(1)
UN = UN[z+1:]
res = 0

for j in TN:
    if j in UN:
        res += 1

print(res)
