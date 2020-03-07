from sys import stdin

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, stdin.readline().split())

d1 = ((Bx-Ax)**2 + (By-Ay)**2) ** 0.5
d2 = ((Dx-Cx)**2 + (Dy-Cy)**2) ** 0.5


