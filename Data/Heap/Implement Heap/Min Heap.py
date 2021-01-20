'''
#### Name:  Implement Heap
Link: [link]()

#### Sub_question_name: Min Heap 
Link: [link]()


**Insertion O(logn) average case O(1)**
**Deletion O(logn) average case O(1)**
**Heapify O(logn)**

'''


class Heap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def get_max(self):
        return self.items[0]

    def display(self):
        print(self.items)

    def insert(self, key):
        index = self.size()  # next free next
        self.items.append(key)

        while (index != 0):   # Keep on updating values with parent, until it finds right place for element
            p = self.parent(index)
            if self.items[p] > self.items[index]:
                self.items[p], self.items[index] = self.items[index], self.items[p]
            index = p

    def min_heapify(self, parent):
        l = self.left(parent)
        r = self.right(parent)
        n = self.size()
        smallest = parent

        if l < n and self.items[l] < self.items[parent]:
            smallest = l
        if r < n and self.items[r] < self.items[parent]:
            smallest = r

        if smallest != parent:
            self.items[smallest], self.items[parent] = self.items[parent], self.items[smallest]
            # heapify the child unitl it is no order
            self.min_heapify(smallest)

    def pop(self):
        if self.size() == 0:
            return None
        min_value = self.items[0]
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.min_heapify(0)  # Heapify with new root
        return min_value


bheap = Heap()

print('Menu')
print('insert <data>')
print('max get')
print('max extract')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'max':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(bheap.get_max()))
        elif suboperation == 'extract':
            print('Maximum value removed: {}'.format(bheap.pop()))

    elif operation == 'show':
        bheap.display()
    elif operation == 'quit':
        break
