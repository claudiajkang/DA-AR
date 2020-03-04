from sys import stdin
read = lambda : stdin.readline().rstrip()

N = int(read())

KOR = {}
ENG = {}
MATH = {}

for i in range(1, N+1):
    na, ko, en, ma = read().split()
    ko, en, ma = map(int, [ko, en, ma])

    if ko not in KOR.keys():
        KOR[ko] = {}

    if en not in KOR[ko].keys():
        KOR[ko][en] = {}

    if ma not in KOR[ko][en].keys():
        KOR[ko][en][ma] = []

    KOR[ko][en][ma].append(na)

for k in sorted(KOR.keys(), reverse=True):
    for e in sorted(KOR[k]):
        for m in sorted(KOR[k][e], reverse=True):
            for n in sorted(KOR[k][e][m]):
                print(n)
