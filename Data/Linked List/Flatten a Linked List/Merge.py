'''
#### Name:  Flatten a Linked List
Link: [link]()

#### Sub_question_name: Merge 
Link: [link]()

## not working
'''


def merge(first, second):

    head = Node(-1)
    cur = head

    while first and second:
        if first.val < second.val:
            cur.right = first
            cur = cur.right
            first = first.down
        else:
            cur.right = second
            second = second.down
            cur = cur.right
    
    while first:
        cur.right = first
        first = first.down
        cur = cur.right
    
    while second:
        cur.right = second
        second = second.down
        cur = cur.right
    
    return head.right

def flatten(head):
    res = merge(head, None)
    cur = head.right
    print_ll(cur)
    while cur:
        res = merge(res, cur)
        # print_ll(res)
        cur = cur.right
    
    return res


class Node:
    def __init__(self, val=None):
        self.val = val
        self.down = None
        self.right = None


start = Node(5)
start.down = Node(7)
start.down.down = Node(8)
start.down.down.down = Node(30)
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
        head = head.right
    print()


print_ll(flatten(start))

# print_ll(start.right)
# print_ll(merge(start, start.right))
