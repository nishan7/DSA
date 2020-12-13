'''
#### Name:  Add two numbers represented by LL
Link: [link]()

#### Sub_question_name: Recursion 
Link: [link]()

**O(n+m) size of liked list SC: O(n)**

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


l1 = ll([9, 9, 9])
l2 = ll([9, 9, 9])
print_ll(l1)
print_ll(l2)

# main program


def add(l1, l2):
    if l1.next == None and l2.next == None:  # Only for the last nodes
        val = l1.val + l2.val
        right_node = None

    elif l1.next != None and l2.next != None:
        right_node, current_carry = add(l1.next, l2.next)
        val = l1.val + l2.val + current_carry

    elif l1.next == None:
        right_node, current_carry = add(l1, l2.next)
        val = l1.val + l2.val + current_carry

    elif l2.next == None:
        right_node, current_carry = add(l1.next, l2)
        val = l1.val + l2.val + current_carry

    if val > 9:
        n = Node(val % 10)
        carry = val // 10
    else:
        n = Node(val)
        carry = 0

    n.next = right_node
    return n, carry


def manage_carry(n, carry):
    if carry == 0:
        return n

    new_node = Node(carry)  # Carry always will be 0 - 1
    new_node.next = n
    return new_node


n, carry = add(l1, l2)
n = manage_carry(n, carry)
print_ll(n)
