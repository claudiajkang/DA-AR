from sys import stdin

n = int(stdin.readline().rstrip())
card = {}

for i in range(n):
    a = int(stdin.readline().rstrip())
    if a not in card.keys():
        card[a] = 0

    card[a] += 1

maxval = max(card.values())

for i in sorted(card.keys()):
    if card[i] == maxval:
        print(i)
        break
