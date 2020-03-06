from sys import stdin
read = lambda : stdin.readline().rstrip()

n = int(read())
st = []

for i in range(n):
    name, k, e, m = read().split()
    st.append((name, int(k), int(e), int(m)))

st.sort(key=lambda item: item[0])
st.sort(key=lambda item: item[3], reverse=True)
st.sort(key=lambda item: item[2])
st.sort(key=lambda item: item[1], reverse=True)

for item in st:
    print(item[0])
