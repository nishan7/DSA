'''
#### Name:  Encapsulation
Link: [link]()

__ double underscore
'''

class Shift:
    def __init__(self):
        self.__manager = ''
        self.size = 0
    
    def setter(self,manager_name, size):
        self.__manager = manager_name
        self.size  = size
    
    def getter(self):
        return self.__manager + " with size "+ str(self.size)


s = Shift()

s.setter('nishan', 5)
print(s.getter())


print(s.size)
# Can't access
# print(s.__manager)

