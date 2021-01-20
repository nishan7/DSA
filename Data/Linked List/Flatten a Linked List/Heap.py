'''
#### Name:  Flatten a Linked List
Link: [link]()

#### Sub_question_name: Heap 
Link: [link]()

'''
from heapq import heappush, heappop
min_heap = []

def flatten(head):
    heappush(min_heap, (head.val, head))
    new_head = Node(-1)
    cur = new_head
    while min_heap:
        value, node = heappop(min_heap)

        cur.right = node
        cur = cur.right
        
        if node.right:
            heappush(min_heap, (node.right.val, node.right))
        
        if node.down:
            heappush(min_heap, (node.down.val, node.down))

    return new_head.right

class Node:
    def __init__(self, val=None):
        self.val = val
        self.down = None
        self.right = None
    
start= Node(5)
start.down= Node(7)
start.down.down = Node(8)
start.down.down = Node(30)
start.right = Node(10)
start.right.down = Node(20)
start.right.right = Node(19)
start.right.right.down = Node(22)
start.right.right.down.down = Node(50)
start.right.right.right = Node(28)
start.right.right.right.down = Node(35)
start.right.right.right.down.down = Node(40)
start.right.right.right.down.down.down = Node(45)

def print_ll(head):
    while head:
        print(head.val, end=" ")
        head= head.right
    print()


print_ll(flatten(start))