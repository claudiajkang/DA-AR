# input
# -9 -9 -9 1 1 1
# 0 -9 0 4 3 2
# -9 -9 -9 1 2 3
# 0 0 8 6 6 0
# 0 0 0 -2 0 0
# 0 0 1 2 4 0


N = 6
TN = 3
RN = 4
tempA = list()

for i in range(N):
    t = [int(s) for s in input().split()]
    tempA.append(t)

arr = [[tempA[j][i] for i in range(N)] for j in range(N)]
# https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python

ncount = [4, 6]
resarr = [[None for i in range(RN)] for j in range(RN)]
# https://stackoverflow.com/questions/9459337/assign-value-to-an-individual-cell-in-a-two-dimensional-python-array/15778885

maxv = {'val': None, 'x': 0, 'y': 0}

for y in range(RN):
    for x in range(RN):
        maxx = x + 2
        maxy = y + 2

        s = 0
        midx = int((x + maxx) / 2)
        midy = int((y + maxy) / 2)

        for ty in range(y, maxy + 1):
            for tx in range(x, maxx + 1):
                if ty == midy and tx != midx:
                    continue
                else:
                    s = s + arr[ty][tx]

        if maxv['val'] == None or maxv['val'] < s:
            maxv['val'] = s
            maxv['x'] = x
            maxv['y'] = y

        resarr[y][x] = s


print(maxv['val'])
