#!/bin/python3

N = input()
h1 = [int(s) for s in input().split()]
h2 = [int(s) for s in input().split()]
h3 = [int(s) for s in input().split()]
s1 = sum(h1)
s2 = sum(h2)
s3 = sum(h3)

while not (s1 == s2 and s2 == s3):
    if s1 > s2 or s1 > s3:
        n1 = h1.pop(0)
        s1 -= n1
    if s2 > s1 or s2 > s1:
        n2 = h2.pop(0)
        s2 -= n2
    if s3 > s1 or s3 > s2:
        n3 = h3.pop(0)
        s3 -= n3

print(s1)


