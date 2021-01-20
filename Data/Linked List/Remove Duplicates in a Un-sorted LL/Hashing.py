'''
#### Name:  Remove Duplicates in a Un-sorted LL.
Link: [link]()

#### Sub_question_name: Hashing 
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


l = ll([1, 5, 1, 6, 3])
print_ll(l)


def duplicates(head):
    visited = set()

    cur = head
    prev = None
    while cur != None:
        if cur.data not in visited:
            visited.add(cur.data)
            prev = cur
            cur = cur.next
        else:  # If visited skip it
            prev.next = cur.next
            prev = cur
            cur = cur.next


duplicates(l)
print_ll(l)
