from sys import stdin

N, B = stdin.readline().strip().split()
alpa = ''
res = 0
B = int(B)
SN = len(N)

for i in range(B):
    if i >= 10:
        alpa += chr(65+(i-10))

    else:
        alpa += str(i)

val = []

for i in range(SN-1, -1, -1):
    val.append(alpa.find(N[i]))

for i, v in enumerate(val):
    res += v * pow(B, i)

print(res)

