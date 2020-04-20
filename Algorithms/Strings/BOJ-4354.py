from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def set_fail(pattern, n):
    fail = [0] * n

    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j

    return fail


for pattern in stdin:
    pattern = pattern[:-1]
    if pattern == '.':
        break

    n = len(pattern)

    fail = set_fail(pattern, n)

    q = fail[n-1]
    r = n - q

    if q == 0 or (q % r != 0):
        print(1)
    else:
        print(q // r + 1)
