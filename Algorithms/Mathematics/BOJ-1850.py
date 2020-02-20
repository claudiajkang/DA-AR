import sys


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    return a


A, B = map(int, sys.stdin.readline().strip().split())
print("1" * gcd(A, B))
