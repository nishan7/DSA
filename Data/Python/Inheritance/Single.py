'''
#### Name:  Inheritance
Link: [link]()

#### Sub_question_name: Single 
Link: [link]()

'''

class Parent():
    def show_parent(self):
        print("This is parent Class")

class Child(Parent):
    def show_child(self):
        print("This is child Class")


p = Parent()
c = Child()

c.show_parent()
c.show_child()