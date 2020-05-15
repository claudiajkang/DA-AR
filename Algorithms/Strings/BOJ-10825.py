from sys import stdin

read = lambda: stdin.readline()

n = int(read())
st = [[] for i in range(n)]

for i in range(n):
    l = read().split()
    st[i] = [l[0], int(l[1]), int(l[2]), int(l[3])]

st.sort(key=lambda x: x[0])
st.sort(reverse=True, key=lambda x: x[3])
st.sort(key=lambda x: x[2])
st.sort(reverse=True, key=lambda x: x[1])

for i in range(n):
    print(st[i][0])
