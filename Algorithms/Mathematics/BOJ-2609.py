from sys import stdin
  
def gcd(a, b):
    if b:
        return gcd(b, a%b)
    else:
        return a

A, B = map(int, stdin.readline().strip().split())
g = gcd(A,B)

print(g)
print(int((A*B)/g))
