'''
#### Name:  Linked List Implementation
Link: [link]()

'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        
        new_node = Node(data)
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def delete_front(self):
        if self.head == None:
            print("Empty")
            return 
        temp = self.head
        self.head = self.head.next
        print("Deleted Value", temp.data)
        temp.next = None

    def delete_last(self):
        if self.head == None:
            print("Empty")
        elif self.head.next == None:
            print("Delete Value:", self.head.data)
            self.head = None
        else:
            cur = self.head
            prev = None
            while cur.next != None:
                prev = cur
                cur = cur.next
            prev.next = None
            print("Deleted Value ", cur.data)

    def delete_key(self, key):
        if self.head == None:
            print("Empty")
        else:
            prev = None
            cur = self.head
            while cur != None:
                prev = cur
                if cur.data == key:
                    break
                cur = cur.next
            else:
                print("Key not found")
                return
            print("Item deleted", cur.data)
            prev.next = cur.next

    def show(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
    
    def _reverse(self, node, prev=None):
        if not node:
            return prev
        next_node = node.next
        node.next = prev
        return self._reverse(next_node, node)





ll = LinkedList()
ll.add_front(5)
ll.add_front(10)
ll.add_last(20)

ll.show()
ll.add_front(55)
ll.show()
ll.add_last(77)
ll.show()
ll.delete_front()
ll.delete_last()
ll.delete_key(4)
ll.show()
s = ll._reverse(ll.head)
ll.head = s
ll.show()
