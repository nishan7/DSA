'''
#### Name:  Inheritance
Link: [link]()

#### Sub_question_name: Hierarchical 
Link: [link]()

'''

class Parent:
    def show_parent(self):
        print("Parent class")


class Child1(Parent):
    def show_child1(self):
        print("Child Class 1")


class Child2(Parent):
    def show_child2(self):
        print("Chid Class 2")



c1 = Child1()
c2 = Child2()

c1.show_child1()
c1.show_parent()

print()

c2.show_child2()
c2.show_parent()

'''
Child Class 1
Parent class

Chid Class 2
Parent class
'''