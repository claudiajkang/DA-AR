from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
read = lambda: stdin.readline().rstrip()


def dfs(num):
    global visited, student, cnt, finished

    visited[num] = True
    if visited[student[num]]:
        if not finished[student[num]]:
            temp = student[num]
            while temp != num:
                temp = student[temp]
                cnt += 1

            cnt += 1

    else: dfs(student[num])
    finished[num] = True


t = int(read())

for tt in range(t):
    n = int(read())
    student = [0] + list(map(int, read().split()))

    visited = [False] * (n+1)
    finished = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    print(n-cnt)