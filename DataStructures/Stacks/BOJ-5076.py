from sys import stdin
read = lambda: stdin.readline().rstrip()

while True:
    w = read()
    if w == "#":
        break

    stack = []

    w = w.replace(" /", "/")
    w = w.replace(" ", "|")
    w = w.replace("<", "|<")
    w = w.replace(">", ">|")
    w = w.split("|")

    for i in w:
        if i == "":
            continue

        elif i[0:2] == "</":
            tt = i.replace("<", "")
            tt = tt.replace(">", "")

            if stack and stack[-1] == tt[1:]:
                stack.pop()
            else:
                stack.append(tt)

        elif i[0] == "<" and i[-2:] == "/>":
            continue

        elif i[0] == "<":
            tt = i.replace("<", "")
            tt = tt.replace(">", "")
            stack.append(tt)

    if stack:
        print("illegal")
    else:
        print("legal")
