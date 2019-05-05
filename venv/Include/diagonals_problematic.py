
def check_line(line: list)->bool:
    count = 1
    tmp = line[0]
    for s in line[1:]:
        if s != tmp:
            count = 1
            tmp = s
        else:
            count += 1
        if count >= 3: return True
    return False

def check_diag(matrix: list)->bool:
    rows = len(matrix)
    cols = len(matrix[0])
    diags = rows + cols - 1
    ldiags = [[] for _ in range(diags)]
    l = 0
    r = 0
    i = 0
    j = 0
    while i <= rows - 1:
        j = 0
        while j <= cols - 1:
            ldiags[l].append(matrix[i][j])
            j += 1
            l += 1
        i += 1
        r += 1
        l = 0 + r

    for line in ldiags:
        if check_line(line): return True

    return False
def checkio(matrix):

    matrix_t = list(zip(*matrix))

    for i, l in enumerate(matrix):
         if check_line(matrix[i]) or check_line(matrix_t[i]):
             return True
    if check_diag(matrix): return True

    for i, l in enumerate(matrix):
        matrix[i]=list(reversed(l))

    if check_diag(matrix): return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
