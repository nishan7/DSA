'''
#### Name:  Implement Stack using Queue
Link: [link]()

#### Sub_question_name: Making Pop Costly 
Link: [link]()

'''

class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, data):
        self.q1.append(data)


    def pop(self):
        # We move all except one form q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(-1))
        
        print(self.q1.pop(-1))
        self.q1, self.q2 = self.q2, self.q1
    
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