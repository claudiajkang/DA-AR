from sys import stdin
read = lambda: stdin.readline().rstrip()

def get_fail(pattern):
    fail = [0] * len(pattern)

    j = 0
    for i in range(1, len(pattern)):
        if j > 0 and pattern[i] != pattern[j]:
            j = fail[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j

    return fail


def kmp(strings, pattern, fail):
    j = 0
    for i in range(len(strings)):
        if j > 0 and strings[i] != pattern[j]:
            j = fail[j - 1]

        if strings[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True

            else:
                j += 1

    return False


a = read()
b = read()
p = read()

fail = get_fail(p)
ra = kmp(a, p, fail)
rb = kmp(b, p, fail)

if ra and rb:
    print('YES')
else:
    print('NO')
