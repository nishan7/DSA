'''
#### Name:  Min Stack (Extra n no extra)
Link: [link]()

#### Sub_question_name: With Extra Space full 
Link: [link]()

Minimum element in the stack

**Time O(1)  Space O(1)**

'''


class SecondaryStack:
    items = [0] * 10
    top = -1
    MS = 10

    def push(self, item):
        if self.top < 10:
            self.top += 1
            self.items[self.top] = item
        else:
            print("Stack Full")

    def pop(self):
        if self.top == -1:
            print("Stack Empty")
        else:
            item = self.items[self.top]
            self.top -= 1
            return item

    def peek(self):
        return self.items[self.top]
    
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


class Stack:
    items = [0] * 10
    top = -1
    MS = 10
    ss = SecondaryStack()

    def push(self, item):
        if self.top < 10:
            self.top += 1
            self.items[self.top] = item

            if self.ss.is_empty() or item <= self.ss.peek():   # Equal size for 3,1,1,pop(), 5 and get_min()
                self.ss.push(item)

        else:
            print("Stack Full")

    def pop(self):
        if self.top == -1:
            print("Stack Empty")
        else:
            item = self.items[self.top]
            self.top -= 1

            if item == self.ss.peek():
                self.ss.pop()
            return item

    def get_min(self):
        if not self.ss.is_empty():
            return self.ss.peek()
        else: 
            None


s = Stack()
s.push(1)
# s.pop()
print(s.get_min())
s.push(-2)
s.push(-2)
s.pop()
s.push(3)

print(s.get_min())
# print(s.pop())
# print(s.pop())
