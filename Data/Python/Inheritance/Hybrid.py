'''
#### Name:  Inheritance
Link: [link]()

#### Sub_question_name: Hybrid 
Link: [link]()

'''

class Parent:
    def show_parent(self):
        print("This is Parent")

    
class Child1(Parent):
    def show_child1(self):
        print("This is child 1")


class Child2(Parent):
    def show_child2(self):
        print("This is child 2")


class Child3(Child1, Child2):
    def show_child3(self):
        print("This is child3")


c = Child3()
c.show_child3()