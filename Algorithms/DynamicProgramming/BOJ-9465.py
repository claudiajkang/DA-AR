from sys import stdin
read = lambda : stdin.readline().rstrip()

T = int(read())

for i in range(T):
    SN = int(read())
    S = [[0] * SN for _ in range(2)]

    for j in range(2):
        S[j] = list(map(int, read().split()))

    R = [[0] * SN for _ in range(2)]
    R[0][0] = S[0][0]
    R[1][0] = S[1][0]

    for j in range(1, SN):
        if j == 1:
            R[0][j] = max(R[1][j-1]+S[0][j], S[0][j])
            R[1][j] = max(R[0][j-1]+S[1][j], S[1][j])
        else:
            R[0][j] = max(R[1][j-2], R[1][j-1]) + S[0][j]
            R[1][j] = max(R[0][j-2], R[0][j-1]) + S[1][j]

    print(max(R[0][-1], R[1][-1]))
