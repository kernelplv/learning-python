def merge(L:list, R:list):
    result = []
    lN, rN = len(L), len(R)
    l, r = 0, 0
    while l < lN and r < rN:
        if L[l] < R[r]:
            result.append(L[l])
            l += 1
        else:
            result.append(R[r])
            r += 1
    return result + L[l:] + R[r:]


def mergesort(stuff: list):
    L = len(stuff)
    if L < 2:
        return stuff
    C = L >> 1
    stuff = merge(mergesort(stuff[:C]), mergesort(stuff[C:]))
    return stuff


def test1():
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print(mergesort(array))

if __name__ == '__main__':
    test1()
    from timeit import Timer
    t = Timer("test1", 'from __main__ import test1')
    print(f'ExE Time: {t.timeit(10):.15f}')
