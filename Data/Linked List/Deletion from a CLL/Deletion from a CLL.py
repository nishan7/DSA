'''
#### Name:  Deletion from a CLL
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


l1 = ll([1, 2, 3, 4, 6, 7])


def delete(head, item):
    if head == None:
        return head

    if head.next == None and head.val == item:
        return None

    cur = head
    prev = None

    while cur:
        if cur.val == item:
            break

        prev = cur
        cur = cur.next

    if prev == None:  # If i want to delete head
        prev = head
        while prev.next != head:  # Set the prev to last element in LL
            prev = prev.next

        head = cur.next   # If head is delete this will be the new nead

    # print(prev.val, cur.val)
    prev.next = cur.next
    print_ll(head)


delete(l1, 1)   # 2 3 4 6 7
# delete(l1, 3)
# delete(l1,3)
