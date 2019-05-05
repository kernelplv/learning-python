# center x0,y0 r - radius
# ( x-x0 ) ^2 + ( y-y0 ) ^2 = r ^2
# prec 2
# короче говоря, метод серединных перпендикуляров..
# если не работает  - ПРОВЕРЬ СКОБКИ
from re import findall as F
from math import sqrt as Q


def checkio(data, lx: list=None, ly: list=None):

    if lx is None:
        x = list()
        y = list()

        for i in F("([0-9],[0-9])", data):
            x.append(float(i[0]))
            y.append(float(i[2]))
    else:
        x = lx
        y = ly

    x.insert(0,0)
    y.insert(0,0)
    print(x, y)

    try:
        Ma = (y[2]-y[1]) / (x[2]-x[1])
        Mb = (y[3]-y[2]) / (x[3]-x[2])
    except ZeroDivisionError:
        x.pop(0)
        y.pop(0)
        x.append(x.pop(0))
        y.append(y.pop(0))
        return checkio(data, x, y)


    print(f'Ma: {Ma:.4f}')
    print(f'Ma: {Mb:.4f}')
    #cross проверить Ма формулу наклонной прямой
    Cx = (Ma * Mb * (y[1] - y[3]) + Mb * (x[1] + x[2]) - Ma * (x[2] + x[3])) / (2 * (Mb - Ma))

    try:
        Cy = - (1 / Ma) * (Cx - ((x[1] + x[2]) / 2)) + (y[1] + y[2]) / 2
    except ZeroDivisionError:
        Cy = - (1 / Mb) * (Cx - ((x[2] + x[3]) / 2)) + (y[2] + y[3]) / 2

    print(f'Center: {Cx},{Cy}')

    r = Q((x[1] - Cx) ** 2 + (y[1] - Cy) ** 2)
    print(f'Radius: {r}')

    answer = f'(x-{Cx:.3g})^2+(y-{Cy:.3g})^2={round(r,2):g}^2'

    print(f'Answer: {answer}')

    return answer

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    assert checkio("(7,7),(4,3),(1,8)") == "(x-3.8)^2+(y-6.28)^2=3.28^2"
    assert checkio("(7,3),(9,6),(3,6)") == "(x-6)^2+(y-5.83)^2=3^2"
    assert checkio("(1,1),(2,1),(1,2)") == "(x-1.5)^2+(y-1.5)^2=0.71^2"
    assert checkio("(9,8),(9,4),(3,6)") == "(x-6.33)^2+(y-6)^2=3.33^2"
    print("good job")
