MODE_AROUND = 1
MODE_DIAG = 2

class Cell:
    def __init__(self, value=0, row=0, col=0):
        self.value = value
        self.pos = {'rows': row,'cols': col}
        self.directions = dict()

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

    def __eq__(self, other: 'Cell'):
        return self.value == other.value

    def get_generated(self):
        current : 'Cell' = self
        strt = self
        dirs = current.directions
        out = list()
        for (d, v) in dirs.items():
            tmp = []
            current = strt
            tmp.append(current)
            while (current is not None):
                current = current.directions.get(d, None)
                if current: tmp.append(current)
            out.append(tmp)
        return out


class SSMC:
    __cells:[]
    rows:int
    cols:int

    def __init__(self, list):

        self.__cells = list
        self.rows = 0
        self.cols = 0

        for i,r in enumerate(list):
            for j, c in enumerate(r):
                self.__cells[i][j] = Cell(c,i,j)
                if self.cols < j: self.cols = j
            if self.rows < i: self.rows = i

    def __iter__(self):
        return iter(self.__cells)

    def __getitem__(self, item):
        return self.__cells[item]

    def __repr__(self):
        return 'rows: ' + str(self.rows) + ' cols: ' + str(self.cols)

    def generate(self, mode=MODE_AROUND):
        Select = {
            MODE_DIAG   : self.__diag_tree
        }

        Select[mode]()


    def __diag_tree(self):
        print ('Generating tree by diagonals...')
        for t in self.__cells:
            for p in t:

                print(f'Processing: {p.pos}')
                i = p.pos['rows']
                j = p.pos['cols']


                while (i < self.rows and j < self.cols):
                    self.__cells[i][j].directions['rd']=self.__cells[i+1][j+1]
                    i += 1
                    j += 1
                i = p.pos['rows']
                j = p.pos['cols']

                while (i > 0 and j > 0):
                    self.__cells[i][j].directions['lu']=self.__cells[i-1][j-1]
                    i -= 1
                    j -= 1
                i = p.pos['rows']
                j = p.pos['cols']

                while (i > 0 and j < self.cols):
                    self.__cells[i][j].directions['ur']=self.__cells[i-1][j+1]
                    i -= 1
                    j += 1
                i = p.pos['rows']
                j = p.pos['cols']

                while (i < self.rows and j > 0):
                    self.__cells[i][j].directions['dl']=self.__cells[i+1][j-1]
                    i += 1
                    j -= 1
                i = p.pos['rows']
                j = p.pos['cols']
        print ('Generating diagonals successful')
