'''
#### Name:  Rotate a DLL in group of Given Size.[Very IMP]
Link: [link]()

'''


def reverse_group(head, k):
    if head == None or head.right == None:
        return head, head, None

    cur = head
    prev = None
    count = 0

    while cur and count < k:
        next_node = cur.right
        cur.left, cur.right = cur.right, cur.left
        prev = cur
        cur = next_node
        count += 1

    return prev, head, next_node


def reverse(head, k):
    start, end, next_group = reverse_group(head, k)
    # print_ll(start)

    group_start = start
    current = end

    while next_group:
        next_group.left = None
        start, end, next_group = reverse_group(next_group, k)
        # print_ll(start)

        current.right = start
        start.left = current

        current = end

    return group_start


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


print_ll(reverse(l1, 3))
