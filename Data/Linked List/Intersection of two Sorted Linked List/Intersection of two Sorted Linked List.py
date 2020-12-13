'''
#### Name:  Intersection of two Sorted Linked List.
Link: [link]()

'''


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def ll(arr):
    start = Node(0)
    cur = start
    for item in arr:
        n = Node(item)
        cur.next = n
        cur = n
    return start.next


def print_ll(cur):
    if cur == None:
        print('Empty')
        return

    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


l1 = ll([1, 2, 3, 4, 6])
l2 = ll([2, 4, 6, 8])
print_ll(l1)
print_ll(l2)

# main program


def intersect(l1, l2):
    head = Node(0)
    cur = head
    while l1 and l2:
        if l1.val == l2.val:
            n = Node(l1.val)
            cur.next = n
            cur = n

            l1 = l1.next
            l2 = l2.next

        elif l1.val < l2.val:
            l1 = l1.next

        else:
            l2 = l2.next

    print_ll(head.next)


intersect(l1, l2)
