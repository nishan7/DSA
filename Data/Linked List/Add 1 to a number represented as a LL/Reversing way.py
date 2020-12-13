'''
#### Name:  Add "1" to a number represented as a LL.
Link: [link]()

#### Sub_question_name: Reversing way 
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


l = ll([9, 9, 9])
print_ll(l)



def reverse_ll(head):
    prev = None
    cur = head

    while cur:
        next = cur.next
        cur.next = prev
        prev= cur
        cur = next
    
    return prev

def add_one(head):
    head = reverse_ll(head)

    carry = 0
    result = Node()

    while head or carry: # Case where ll is empty but still carry is present
        carry += head.value

        temp = Node(carry % 10)
        carry - carry // 10
    




add_one(l)
# l = reverse_ll(l)
print_ll(l)