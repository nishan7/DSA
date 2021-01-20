'''
#### Name:  Inheritance
Link: [link]()

#### Sub_question_name: Multiple 
Link: [link]()

'''

class Parent1():
    def show(self):
        print("This is Parent1")

class Parent2():
    def show(self):
        print("This is Parent2")


class Child(Parent1, Parent2):
    pass
    # def show(self):
    #     print("This is Child")


c = Child()
c.show()