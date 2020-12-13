'''
#### Name:  Constructers
Link: [link]()

Only one constructor, as always second "__init__" class will be choosed as a constructor

'''


class Rect:

    def __init__(self):
        self._length = 0
        self.breath = 0

    def print_values(self):
        print(self._length, self.breath)


r = Rect()
r.print_values()


class Rect2:

    def __init__(self, a, b):
        self.length = a
        self.breath = b

    def print_values(self):
        print(self.length, self.breath)


r2 = Rect2(5, 10)
r2.print_values()


class Rect3:

    def __init__(self, obj):
        self.length = obj.length
        self.breath = obj.breath

    def print_values(self):
        print(self.length, self.breath)


r3 = Rect3(r2)
r3.print_values()
