'''
#### Name:  Rotate DLL by N nodes.
Link: [link]()


1) 1 <> 2 <> 3 <> 4 <> 5 <> 6 
2) 1 <> 2     3 <> 4 <> 5 <> 6
3) 3 <> 4 <> 5 <> 6 <> 1 <> 2

'''


def rotate(head, n):
    cur = head

    # Step 1 Search the nth and n+1th element
    prev = None
    while n > 0 and cur != None:
        prev = cur
        cur = cur.right
        n -= 1

    # if the linked list is small return input as output
    if cur == None:
        return head


    #   Step 2; separate the front and back part
    start = head
    end = prev
    head = cur
    end.right = None
    cur.left = None

    # Step 3 find the end of the linkedin list
    while cur.right != None:
        cur = cur.right

    cur.right = start
    start.left = cur

    return head


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


nums = ll([1, 2, 3, 4, 5, 6])
nums = ll([1, 2, 3])
print_ll(nums)
print_ll(rotate(nums, 2))
