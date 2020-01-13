stack = list()
N = int(input())
max = -1

for i in range(N):
    t = input().split()
    q = int(t[0])

    if q is 1:
        v = int(t[1])
        if max < v:
            max = v
        stack.append(v)

    elif q is 2:
        v = stack.pop()
        if v is max:
            max = -1

            for j in range(len(stack)):
                if max < stack[j]:
                    max = stack[j]

    elif q is 3:
        print(max)

