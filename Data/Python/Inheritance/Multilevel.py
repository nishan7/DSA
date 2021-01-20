'''
#### Name:  Inheritance
Link: [link]()

#### Sub_question_name: Multilevel 
Link: [link]()

'''


class Level1:
    def show1(self):
        print("This is level 1")


class Level2(Level1):
    def show2(self):
        print("This is level 2")


class Level3(Level2):
    def show3(self):
        print("This is level 3")


l3 = Level3()

l3.show1()
l3.show2()
l3.show3()

'''
This is level 1
This is level 2
This is level 3

'''