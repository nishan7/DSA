'''
#### Name:  Reverse a DLL.
Link: [link]()

'''


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def ll(arr):
    start = Node(arr[0])
    cur = start
    for item in arr[1:]:
        n = Node(item)
        cur.right = n
        n.left = cur
        cur = n

    return start


def print_ll(cur):
    if cur == None:
        print('Empty')
        return

    while cur:
        print(cur.val, end=" ")
        cur = cur.right
    print()


l1 = ll([1, 2, 3, 2, 1])
l2 = ll([2, 4, 6, 8])
# print_ll(l1)
print_ll(l2)


def reverse(head):
    if head == None or head.right == None:
        return head

    cur = head
    prev = None
    while cur:
        next_node = cur.right
        cur.left, cur.right = cur.right, cur.left
        prev = cur
        cur = next_node

    return prev


print_ll(reverse(l2))
