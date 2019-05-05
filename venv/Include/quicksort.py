def quicksort(arr: list=None):

    L = len(arr)
    i, j = 0, L - 1
    c = arr[ (L - 1) >> 1 ]
    stop = True

    while stop:
        while ( arr[i] < c ): i += 1
        while ( arr[j] > c ): j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            stop = i <= j
    if j > 0:
        arr[:j] = quicksort(arr[:j])
    if i < L:
        arr[i:] = quicksort(arr[i:])

    return arr


if __name__ == '__main__':
    from timeit import Timer
    array = [1, 4, 2, 8]
    print(f"QuickSort:\n before: {array}\n after: {quicksort(array)}")
    t = Timer("quicksort",'from __main__ import quicksort')
    print(f'ExE Time: {t.timeit(5):.8f}')
