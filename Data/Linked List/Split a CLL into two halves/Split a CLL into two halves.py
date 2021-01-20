'''
#### Name:  Split a CLL into two halves.
Link: [link]()

Similar to floyd hare tortosie technique

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
    cur.next = start.next
    return start.next


def print_ll(cur):
    head = cur
    if cur == None:
        print('Empty')
        return

    while cur.next != head:
        print(cur.val, end=" ")
        cur = cur.next
    print(cur.val, end=" ")
    print()


l1 = ll([1, 2, 3, 4, 6])
l3 = ll([1, 2, 3, 4, 6, 7])
l2 = ll([2, 4])
# print_ll(l1)
# print_ll(l2)


def split(head):
    fast = slow = head

    while fast.next != head and fast.next.next != head:  # Fast goes to last or second last char
        fast = fast.next.next
        slow = slow.next

    if fast.next == head:  # If fast is last node
        last = fast
    elif fast.next.next == head:  # If fast is second last node
        last = fast.next

    second = slow.next
    last.next = second

    first = head
    slow.next = first

    print_ll(first)
    print_ll(second)
    print()


split(l1)
split(l2)
split(l3)
