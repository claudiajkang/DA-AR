def Query1(x, y, la, N, S):
    seq = (x ^ la) % N
    S[seq].append(y)


def Query2(x, y, la, N, S):
    seq = (x ^ la) % N
    tla = y % len(S[seq])
    return S[seq][tla]


t = input().split()
N, Q = int(t[0]), int(t[1])
lastAnswer = 0
S = list()

for i in range(N):
    templist = list()
    S.append(templist)

for i in range(Q):
    t = input().split()
    qn, x, y = int(t[0]), int(t[1]), int(t[2])

    if qn == 1:
        Query1(x, y, lastAnswer, N, S)


    elif qn == 2:
        lastAnswer = Query2(x, y, lastAnswer, N, S)
        print(lastAnswer)
