class Number:
    value: int
    operation: str = '+'

    def get_value(self):
        return self.value

    def __init__(self, value: int, op: str = '+'):
        self.value = value
        self.operation = op

    @property
    def plus(self):
        return Number(self.value, '+')

    @property
    def minus(self):
        return Number(self.value, '-')

    @property
    def times(self):
        return Number(self.value, '*')

    @property
    def zero(self):
        return Number(eval(f'{self.value} {self.operation} 0'))

    @property
    def one(self):
        return Number(eval(f'{self.value} {self.operation} 1'))

    @property
    def two(self):
        return Number(eval(f'{self.value} {self.operation} 2'))

    @property
    def three(self):
        return Number(eval(f'{self.value} {self.operation} 3'))

    @property
    def four(self):
        return Number(eval(f'{self.value} {self.operation} 4'))

    @property
    def five(self):
        return Number(eval(f'{self.value} {self.operation} 5'))

    @property
    def six(self):
        return Number(eval(f'{self.value} {self.operation} 6'))

    @property
    def seven(self):
        return Number(eval(f'{self.value} {self.operation} 7'))

    @property
    def eight(self):
        return Number(eval(f'{self.value} {self.operation} 8'))

    @property
    def nine(self):
        return Number(eval(f'{self.value} {self.operation} 9'))

    def __repr__(self):
        return str(self.value)


# Создаем экземпляры для чисел от 0 до 9
zero = Number(0)
one = Number(1)
two = Number(2)
three = Number(3)
four = Number(4)
five = Number(5)
six = Number(6)
seven = Number(7)
eight = Number(8)
nine = Number(9)

print(zero.plus.one.minus.one) # 0
