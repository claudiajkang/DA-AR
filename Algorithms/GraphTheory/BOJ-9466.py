import sys
sys.setrecursionlimit(111111)


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)  # 사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]

    if visited[number]:  # 방문가능한 곳이 끝났는지
        if number in cycle:  # 사이클 가능 여부
            result += cycle[cycle.index(number):] # 사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N  # 방문 여부
    result = []

    for i in range(1, N + 1):
        if not visited[i]:  # 방문 안한 곳이라면
            cycle = []
            dfs(i)  # DFS 함수 돌림

    print(N - len(result))  # 팀에 없는 사람 수