'''
#### Name:  Linked List Implementation
Link: [link]()

#### Sub_question_name: Double 
Link: [link]()

A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.

Operations
- InsertFront, InsertLast, InsertAfter
- DeleteFront, DeleteLast, Delete_key
- display, display_reverse


'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def insertFront(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            return

        # Attach to front
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertLast(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            return

        cur = self.head
        while cur.next != None:
            cur = cur.next

        cur.next = node
        node.prev = cur

    def insertAfter(self, key, data):
        cur = self.head

        while cur:
            if cur.data == key:
                node = Node(data)
                after_node = cur.next
                node.next = after_node
                after_node.prev = node
                cur.next = node
                node.prev = cur
                return
            cur = cur.next
        print('{} not found in DLL'.format(key))

    def deleteFront(self):
        if self.head == None:
            print('Empty')
        print(self.head.data, 'is deleted')
        self.head = self.head.next
        self.head.prev = None

    def deleteLast(self):
        if self.head == None:
            print('Empty')

        cur = self.head
        while cur.next:
            cur = cur.next

        print(cur.data, 'is deleted')
        prev = cur.prev
        prev.next = None

    def delete(self, key):
        if self.head == None:
            print('Empty')

        cur = self.head
        while cur:
            if cur.data == key:
                print(cur.data, 'is deleted')
                prev = cur.prev
                next = cur.next

                prev.next = next
                next.prev = prev
                return

            cur = cur.next
        print('{} not found in DLL'.format(key))

    def display(self):
        cur = self.head

        while cur != None:
            print(cur.data, end=" ")
            cur = cur.next

    def display_reverse(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next

        while cur:
            print(cur.data, end=" ")
            cur = cur.prev


dll = DLL()
dll.insertFront(5)
dll.insertFront(10)
dll.insertLast(15)
dll.insertAfter(10, 22)
dll.display()
print()
dll.delete(22)
dll.display()
print()
dll.display_reverse()
