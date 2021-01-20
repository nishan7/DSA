'''
#### Name:  Intersection Point of two Linked Lists.
Link: [link]()

#### Sub_question_name: Sets(hashing) 
Link: [link]()

'''


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def print_ll(cur):
    if cur == None:
        print('Empty')
        return

    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


l1 = Node(5)
l1.next = Node(6)
l1.next.next = Node(7)
l1.next.next.next = Node(8)

l2 = Node(11)
l2.next = Node(22)
l2.next.next = l1.next.next.next
l2.next.next.next = Node(99)
l2.next.next.next.next = Node(999)
print_ll(l1)
print_ll(l2)

# main program


def intersect(l1, l2):
    visited = set()

    while l1:
        visited.add(l1)
        l1 = l1.next

    while l2:
        if l2 in visited:
            return l2

        l2 = l2.next


print_ll(intersect(l1, l2))
