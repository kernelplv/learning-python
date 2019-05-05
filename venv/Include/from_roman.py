def reverse_roman(romans: str)-> int:
    R = dict([
        ('CM', 900),
        ('CD', 400),
        ('XC', 90),
        ('XL', 40),
        ('IX', 9),
        ('IV', 4),
        ('M',    1000),
        ('D',    500),
        ('C',    100),
        ('L',     50),
        ('X',     10),
        ('V',     5),
        ('I',     1)
         ])
    result = 0

    while romans.__len__() > 0:

        for d in R.keys():
            fnd = romans.find(d)
            if fnd == 0:
                result += R[d]
                romans = romans[len(d):]
                break
            else:
                continue

    print(result)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    assert reverse_roman('MMMCMXCIX') == 3999, '3999'
    print('Great! It is time to Check your code!');