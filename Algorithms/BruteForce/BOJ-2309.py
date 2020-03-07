from sys import stdin

H = [0] * 9

for i in range(9):
    H[i] = int(stdin.readline())

H = sorted(H)
S = 100
res = []
diff = sum(H) - 100

for i in range(9):
    for j in range(9):
        if i != j:
            if H[i] + H[j] == diff:
                res.append([i, j])
                break

    if len(res) > 0:
        for i, j in res:
            for ii in range(9):
                if ii not in [i, j]:
                    print(H[ii])
            break
        break
