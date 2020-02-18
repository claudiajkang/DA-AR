from sys import stdin
  
def gcd(a, b):
    if b:
        return gcd(b, a%b)
    return a

A, B = map(int, stdin.readline().strip().split())
g = gcd(A,B)
print(int(g))
print(int((A*B)/g))
