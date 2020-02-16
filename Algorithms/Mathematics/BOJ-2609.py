from sys import stdin

A, B = map(int, stdin.readline().strip().split())

def gcd(a,b):
    v1, v2 = A, B
    if A < B:
        v1, v2 = B, A
    
    mod = v1 % v2

    while mod > 0:
        v1 = v2
        v2 = mod
        mod = v1 % v2
    
    return v2

print(gcd(A,B))

print(int((A*B)/gcd(A,B)))
