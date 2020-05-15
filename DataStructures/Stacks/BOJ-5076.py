from sys import stdin

while True:
    wd = stdin.readline().rstrip()
    if wd == "#": break
    s = []
    wd = wd.replace(" />", "/>").replace("<", "|<").replace(">", ">|").split("|")
    for w in wd:
        if w == "" or w == " ": continue
        elif w[:2] == "</" and w[-1] == ">":
            if s and s[-1] == w[2:-1]: s.pop()
            else: s.append(w[1:])
        elif w[0] == "<" and w[-2:] == "/>": continue
        elif w[0] == "<" and w[-1] == ">":
            w = w.split()
            if len(w) > 1: s.append(w[0][1:])
            else: s.append(w[0][1:-1])
    print("illegal" if s else "legal")
