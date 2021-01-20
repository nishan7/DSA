'''
#### Name:  Add two numbers represented by LL
Link: [link]()

#### Sub_question_name: Iterative 
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


l1 = ll([8, 8])
l2 = ll([9, 9, 9])
print_ll(l1)
print_ll(l2)

# main program


def add(l1, l2):
    s1 = []
    s2 = []
    while l1:
        s1.append(l1.val)
        l1 = l1.next

    while l2:
        s2.append(l2.val)
        l2 = l2.next

    carry = 0
    right_node = None
    while s1 or s2 or carry:
        if s1 and s2:
            val = s1.pop() + s2.pop() + carry
        elif s1:
            val = s1.pop() + carry
        elif s2:
            val = s2.pop() + carry
        elif carry:
            val = carry

        val, carry = val % 10, val // 10

        new_node = Node(val)
        new_node.next = right_node
        right_node = new_node

    print_ll(right_node)


add(l1, l2)  # 1087
# print_ll(n)
