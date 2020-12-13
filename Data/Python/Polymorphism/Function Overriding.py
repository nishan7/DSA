'''
#### Name:  Polymorphism
Link: [link]()

#### Sub_question_name: Function Overriding 
Link: [link]()

'''

class Animal:
    def speak(self):
        # return 'Sound'
        pass

class Dog(Animal):
    def speak(self):
        return 'Woof'


class Cat(Animal):
    def speak(self):
        return 'Meow'



d = Dog()
c = Cat()

print(d.speak(), c.speak())