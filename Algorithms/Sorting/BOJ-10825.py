from sys import stdin
read = lambda : stdin.readline().rstrip()

N = int(read())
st = []

for i in range(N):
    name, ko, en, ma = read().split()
    st.append([name, int(ko), int(en), int(ma)])

st.sort(key=lambda x : x[0])
st.sort(key=lambda x : x[3], reverse=True)
st.sort(key=lambda x : x[2])
st.sort(key=lambda x : x[1], reverse=True)

for name, ko, en, ma in st:
    print(name)
