'''
#### Name:  Implement Stack using Queue
Link: [link]()

#### Sub_question_name: Making Push Costly 
Link: [link]()

'''


class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, data):
        # Append in empty q2
        self.q2.append(data)

        # Insert all the values from q1 to q2
        while self.q1:
            self.q2.insert(0, self.q1.pop(-1))

        # Replace self.q1 and self.q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        print(self.q1.pop(-1))

    def display(self):
        print(self.q1)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.pop()
s.pop()
