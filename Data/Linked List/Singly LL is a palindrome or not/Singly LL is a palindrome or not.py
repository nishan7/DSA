'''
#### Name:  Singly LL is a palindrome or not?
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


l1 = ll([1, 2, 3, 2, 1])
l2 = ll([2, 4, 6, 8])
# print_ll(l1)
print_ll(l2)


def check_palin(head):
    stack = []
    cur = head

    while cur:
        stack.append(cur.val)
        cur = cur.next

    cur = head
    while stack:
        if cur.val != stack.pop():
            return False

        cur = cur.next

    return True


print(check_palin(l1))
