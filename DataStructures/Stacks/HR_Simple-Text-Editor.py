N = int(input())
S = ""
undo = list()
undo.append(S)

for i in range(N):
    inputs = input().split()
    q = int(inputs[0])

    if q == 1:
        undo.append(S)
        S = S + inputs[1]

    elif q == 2:
        undo.append(S)
        v = int(inputs[1])
        for j in range(v):
            tlen = len(S)
            S = S[:tlen-1]

    elif q == 3:
        v = int(inputs[1])-1
        print(S[v])

    elif q == 4:
        S = undo.pop()

