s = int(input())
strings = list()
queries = list()

for i in range(s):
    t = input()
    strings.append(t)

q = int(input())

for i in range(q):
    t = input()
    queries.append(t)


for tq in queries:
    c=0
    for ts in strings:
        if ts in tq:
            c=c+1

    print(c)

