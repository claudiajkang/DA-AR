import sys

MAX = 1000000
prime = [True for _ in range(MAX+1)]

for i in range(2, MAX+1):
    if i*i > MAX:
        break
    if prime[i]:
        for j in range(i*i, MAX+1, i):
            prime[j] = False

while True:
    n = int(sys.stdin.readline().strip())
    if n is 0:
        break
    for i in range(2, MAX+1):
        if prime[i]:
            if prime[n - i]:
                print(n, "=", i, "+", n - i)
                break
