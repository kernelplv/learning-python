class Pyramid:
    id: int
    left: 'Pyramid'
    right: 'Pyramid'
    value: object
    lastuse: bool

    class _Getirator:
        items: list

        def __init__(self):
            self.items = list()

        def push(self, value):
            self.items.append(value)

    def __init__(self, value=None):
        self.time_to_build = False
        self.id = 0
        self.value = value
        self.lastuse = False
        self.left = None
        self.right = None

    def add(self, value, invert: bool=False):
        new = Pyramid(value)
        new.id = self.id + 1

        if invert:
            if new.value > self.value:
                new.value, self.value = self.value, new.value
        else:
            if new.value < self.value:
                new.value, self.value = self.value, new.value

        if not self.left:
            self.left = new
            return
        if not self.right:
            self.right = new
            return
        if not self.left.lastuse:
            self.left.add(new.value)
            self.left.lastuse = True
            self.right.lastuse = False
            return
        if not self.right.lastuse:
            self.right.add(new.value)
            self.right.lastuse = True
            self.left.lastuse = False
            return

    def getlist(self, get: '_Getirator'=None):
        if get is None:
            get = self._Getirator()
        get.push(self.value)
        if self.left:
            self.left.getlist(get)
        if self.right:
            self.right.getlist(get)
        return get.items


def sort(arr: list, count: int=1):
    if count > 0:
        T = Pyramid(arr[0])
        for i in arr[1:]:
            T.add(i)
        yield T.value
        yield from sort(T.getlist()[1:], count - 1)


def test1():
    array = [3, 15, 11, 6, 9, 14, 10, 12, 1, 7, 8, 2, 13, 4, 5]
    print(f'Array: \t\t{array}')
    T = sort(array, 15)
    print(f"HeapSort:\n before: \t{array}\n after: \t{list(T)}")

if __name__ == '__main__':
    # todo: короче: верхушку дерева в конец массива и так п-1 раз
    test1()
    from timeit import Timer
    t = Timer("test1", 'from __main__ import test1')
    print(f'ExE Time: {t.timeit(10):.8f}')
