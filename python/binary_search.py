def binary_search(a, v):
    l = 0
    r = len(a) - 1

    while r >= l:
        m = l + (r - l) // 2

        if v == a[m]:
            return m
        elif v < a[m]:
            r = m - 1
        else:
            l = m + 1

    return -1


a = [1, 3, 5, 30, 42, 43, 500]
v = 500
i = binary_search(a, v)
print(i)
