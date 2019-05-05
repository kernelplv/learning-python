def insertsort(A:list, I:int=1):

    if I >= len(A): return A
    while A[I]< A[I-1] and I > 0:
        A[I], A[I-1] = A[I-1], A[I]
        I -= 1
    else:
        I += 1
    return insertsort(A, I)


def swap(A,B):
    A, B = B, A
def test1():
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print(insertsort(array))

if __name__ == '__main__':
    test1()
    from timeit import Timer
    t = Timer("test1", 'from __main__ import test1')
    print(f'ExE Time: {t.timeit(5):.15f}')
    0.000001138000000
    0.000000854000000