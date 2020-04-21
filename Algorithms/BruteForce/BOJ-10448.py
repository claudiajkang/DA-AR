from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()

def trinum(v):
    global pn
    for i in pn:
        for j in pn:
            for k in pn:
                if (i+j+k) == v:
                    return 1

    return 0

t = int(read())
test = [int(read()) for i in range(t)]
MAX = 45

pn = [1] * MAX

for i in range(2, MAX):
    pn[i] = (i * (i+1)) // 2

pn = pn[1:]

for i in test:
    print(trinum(i))