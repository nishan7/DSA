'''
#### Name:  Implement 2 stack in an array
Link: [link]()

One stack from front another from back

**Push O(1) Pop O(1) Space: O(n)**
'''


class Stack:

    def __init__(self):
        self.top1 = -1
        self.MS = 5
        self.top2 = self.MS
        self.items = [0] * self.MS

    def push1(self, data):
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.items[self.top1] = data
        else:
            print("Stack Overflow")

    def pop1(self):
        if self.top1 == -1:
            print("Stack Empty")
        else:
            print(self.items[self.top1])
            self.top1 -= 1

    def push2(self, data):
        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.items[self.top2] = data
        else:
            print("Stack Overflow")

    def pop2(self):
        if self.top2 == self.MS:
            print("Stack Empty")

        else:
            print(self.items[self.top2])
            self.top2 += 1

s = Stack()
s.push1(1)
s.push1(2)
s.push1(3)