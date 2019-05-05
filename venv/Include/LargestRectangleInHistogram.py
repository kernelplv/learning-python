def smartrectstack(push: int=0, reset: bool= False):
    # todo: no 'for' no 'while' - when 'if' is life
    if not hasattr(smartrectstack,'__init'):
        smartrectstack.sum = 0
        smartrectstack.__stack = list()
        smartrectstack.__init = True
    if reset: #clear before new sequence
        smartrectstack.__stack[:] = []
        if push == 0: #clear before new target
            smartrectstack.sum = 0
        return
    else:
        if smartrectstack.__stack.__len__() == 0:
            smartrectstack.__stack.append(push)
        else:
            last = smartrectstack.__stack.pop()
            if last > push:
                smartrectstack.__stack = [push] * (len(smartrectstack.__stack)+ 2)
            elif last < push:
                smartrectstack.__stack.append(last)
                smartrectstack.__stack.append(last)
            else:
                smartrectstack.__stack.append(push)
                smartrectstack.__stack.append(last)
            print(smartrectstack.__stack)
        sm = sum(smartrectstack.__stack)
        if sm > smartrectstack.sum:
            smartrectstack.sum = sm
    return sm

def largest_histogram(histogram):
    mx = len(histogram)
    if max(histogram) > mx:
        mx = max(histogram)
    smartrectstack(0, True)
    for idx, val in enumerate(histogram):
        for l in histogram[idx:]:
            smartrectstack(l)
        smartrectstack(999, True)
        print(smartrectstack.sum)
    return smartrectstack.sum


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert largest_histogram([0,1,2,3,4,5,6,5,4,3,2,1,0]) == 21
    print("Done! Go check it!")