from sys import stdin

w, m, k = map(int, stdin.readline().split())

if w < 2:
    print(0)
    exit()

team = w // 2
if team > m:
    team = m

wr = w - 2*team
mr = m - team
r = wr + mr

while r < k:
    team -= 1
    r += 3

print(team)
