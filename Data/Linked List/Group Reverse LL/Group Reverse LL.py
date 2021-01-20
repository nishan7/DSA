'''
#### Name:  Group Reverse LL
Link: [link]()

'''


class Node:
    def __init__(self, data=None):
        self.data = data
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
        print(cur.data, end=" ")
        cur = cur.next
    print()


def rev(cur, k):
    # Reverse k node and return it
    head = cur

    prev = None
    while cur != None and k > 0:
        k -= 1
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    # prev(starting element), head(end node of reversed ll), cur (new starting point of next group)
    return prev, head, cur


def reverse(head, k):

    first_start, first_end, next_group = rev(head, k)
    cur = first_end

    while next_group != None:
        start, end, next_group = rev(next_group, k)
        cur.next = start
        cur = end

    print_ll(first_start)


l = ll([1, 2, 2, 4, 5, 6, 7, 8])
reverse(l, 4)
