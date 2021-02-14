'''
#### Name:  Remove Duplicates in a Un-sorted LL.
Link: [link]()

#### Sub_question_name: Brute 
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
    i = head

    while i:
        j = i.next
        prev = i

        while j:
            if j.data == i.data:
                prev.next = j.next

            prev = j
            j = j.next
            
        i = i.next

duplicates(l)
print_ll(l)





# def duplicates(head):
#     # equalivlent to i -> (1,n) ; j -> (i)
#     i = head.next
#     j = head
#     prev = head  # We will delete, and not try to delete head

#     while i != None:
#         j = head

#         while j != i and j != None:
#             if i.data == j.data:
#                 prev.next = i.next
#                 # del i
#             j = j.next

#         print()
#         prev = i
#         i = i.next