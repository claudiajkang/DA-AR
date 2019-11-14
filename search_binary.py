def binary_search_rec(seq, target, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    if target == seq[mid]:
        return mid
    elif target < seq[mid]:
        return binary_search_rec(seq, target, low, mid - 1)
    else:
        return binary_search_rec(seq, target, mid + 1, high)


def binary_search_iter(seq, target):
    high, low = len(seq), 0
    while low < high:
        mid = (high + low) // 2
        if target == seq[mid]:
            return mid
        elif target < seq[mid]:
            high = mid
        else:
            low = mid + 1

    return None


def resprint(res, val):
    if res is None:
        print(str(val) + ": X")

    else:
        print(str(val) + ": O")


plist = [1, 2, 5, 6, 7, 10, 12, 14, 15]
val = 12
res = binary_search_iter(plist, 12)
resprint(res, 12)
