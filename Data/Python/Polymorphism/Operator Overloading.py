'''
#### Name:  Polymorphism
Link: [link]()

#### Sub_question_name: Operator Overloading 
Link: [link]()

'''


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return '{}i{}j'.format(self.a, self.b)
        else:
            return '{}i+{}j'.format(self.a, self.b)

    def __add__(self, other):
        return Complex(self.a+other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)


c1 = Complex(5, 6)
c2 = Complex(11, -11)

print(c1, c2)

c3 = c1 + c2

print(c3)
