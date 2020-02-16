from sys import stdin

A, B, C = map(int, stdin.readline().strip().split())

print((A + B) % C)
print((A % C + B % C ) % C)
print((A * B) % C)
print((A % C * B % C) % C)
