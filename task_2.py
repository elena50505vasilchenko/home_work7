from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Абстрактное'


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Для пальто необходимо: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Абстрактное'


class Costume(Clothes):
    @property
    def consumption(self):
        return f'Для костюма необходимо: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        return 'Абстрактное'


coat = Coat(80)
costume = Costume(35)
print(costume.consumption)
print(coat.consumption)