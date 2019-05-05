class ceed:
    root:  str
    left:  'ceed'
    right: 'ceed'
    crown: list()

    def __init__(self, root='', crown=list()):
        self.root = root
        self.left = None
        self.right = None
        self.crown = crown

    def water(self):
        if self.root == self.root[::-1]:
            self.crown.append(self.root)
            #print(self.root)
        else:
            if self.root:
                self.left = ceed(self.root[:-1], self.crown)
                self.right = ceed(self.root[1:], self.crown)

            if self.left : self.left.water()
            if self.right: self.right.water()

def longest_palindromic(text):

    flower = ceed(text, list())
    flower.water()
    print(flower.crown)
    print(max(flower.crown,key=len))

    mirrorstring = max(flower.crown, key=len)

    return mirrorstring


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"