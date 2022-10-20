from sys import stdin


class Matrix(list):
    def __init__(self, L):
        self.L = [line.copy() for line in L]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.L])

    def size(self):
        return len(self.L), len(self.L[0])

    def __add__(self, other):
        ri, rj = range(len(self.L)), range(len(self.L[0]))
        return Matrix([[self.L[i][j] + other.L[i][j] for j in rj] for i in ri])

    def __mul__(self, skal):
        ri, rj = range(len(self.L)), range(len(self.L[0]))
        return Matrix([[self.L[i][j] * skal for j in rj] for i in ri])

    __rmul__ = __mul__


exec(stdin.read())
