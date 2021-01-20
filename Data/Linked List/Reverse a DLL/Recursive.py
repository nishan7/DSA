'''
#### Name:  Reverse a DLL.
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

'''

def reverse(head, prev = None):
    if head == None:
        return head

    next_node = head.right
    head.left , head.right = head.right, head.left

    if next_node == None:
        return head
    return reverse(next_node, head)  
  


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




print_ll(reverse(l2))

