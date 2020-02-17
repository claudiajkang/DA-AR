from sys import stdin

def gcd(a,b):
    if b:
        return gcd(b, a%b)
    return a

N = int(stdin.readline())

for i in range(N):
    A, B = map(int, stdin.readline().strip().split())
    print(int((A*B)/gcd(A,B)))

