class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return f'Размер клетки - {self.num + other.num}'

    def __sub__(self, other):
        sub = self.num - other.num
        return f'Tеперь клетка равна {sub} клеточкам' if sub > 0 else 'Клетки нет'

    def __truediv__(self, other):
        return self.num // other.num

    def __mul__(self, other):
        return self.num * other.num

    def make_order(self, row):
        result = ''
        for i in range(int(self.num / row)):
            result += '*' * row + '\n'
        result += '*' * (self.num % row) + '\n'
        return result


cell_1 = Cell(111)
cell_2 = Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(8))