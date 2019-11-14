def linearsearch(olist, val):
    if olist.count(val) > 0:
        return True

    return False


def resprint(res, val):
    ps = str(val) + ": "

    if res:
        ps = ps + "O"

    else:
        ps = ps + "X"

    print(ps)


plist = [1, 5, 6, 8, 3]
fv = 6
res = linearsearch(plist, fv)
resprint(res, fv)
print("---")
fv = 10
res = linearsearch(plist, fv)
resprint(res, fv)
