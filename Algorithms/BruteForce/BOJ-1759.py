from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()


def backtrace(pos, prev, cons, vowel):
    global L, P, C, A, isVowel
    if pos == L:
        if cons >= 2 and vowel >= 1:
            print(''.join(P))
        return

    for i in range(prev+1, C):
        P[pos] = A[i]
        backtrace(pos+1, i, cons + (not isVowel[ord(A[i])-97]), vowel + isVowel[ord(A[i])-97])


L, C = map(int, read().split())
A = read().split()
A.sort()
P = [''] * C

isVowel = [False] * 26

for i in [0, 4, 8, 14, 20]:
    isVowel[i] = True

backtrace(0, -1, 0, 0)