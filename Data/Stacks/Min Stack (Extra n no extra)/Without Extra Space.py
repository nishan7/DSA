'''
#### Name:  Min Stack (Extra n no extra)
Link: [link]()

#### Sub_question_name: Without Extra Space 
Link: [link](https://www.youtube.com/watch?v=ZvaRHYYI0-4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=11)

Every continers are O(n) like stack,queues   
Only Variables are O(1) 

Using 2*x - min_element, to push flag


# TODO: using list and push pop functions
'''


class Stack:
    items = [0] * 10
    top = -1
    MS = 10
    min_elem = -1

    def push(self, item):
        if self.top < 10:

            if self.min_elem == -1:
                self.top += 1
                self.items[self.top] = item
                self.min_elem = item

            elif item >= self.min_elem:
                self.top += 1
                self.items[self.top] = item

            elif item < self.min_elem:
                val = 2*item - self.min_elem
                self.top += 1
                self.items[self.top] = item
                self.min_elem = item

        else:
            print("Stack Full")

    def pop(self):
        if self.top == -1:
            print("Stack Empty")
        else:
            ans = self.items[self.top]
            self.top -= 1

            if ans == self.min_elem:  # It means the the stack has a flag
                ans = 2 * ans - self.min_elem
            return ans

    def get_min(self):
        if self.min_elem != -1:
            return self.min_elem
        else:
            return None

    def display(self):
        print(self.items, self.top, self.min_elem)


s = Stack()
s.push(11)
# s.pop()
print(s.get_min())
# s.display()
s.push(2)
s.push(2)
s.display()
s.pop()
s.push(3)

print(s.get_min())
# print(s.pop())
# print(s.pop())
