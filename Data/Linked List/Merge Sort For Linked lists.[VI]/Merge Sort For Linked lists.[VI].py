'''
#### Name:  Merge Sort For Linked lists.[VI]*
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


l1 = ll([1, 21, 3, 11, 4, 6, 2])
left = ll([1, 3, 4, 7])
right = ll([2, 5])
# print_ll(l1)


# main program
def find_middle(l1):

    slow = l1
    fast = l1

    while fast.next and fast.next.next:  # [2,5] 5 is middle value
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left, right):
    if left == None:
        return right

    if right == None:
        return left

    res = Node(-11)
    cur = res

    while left and right:
        if left.val <= right.val:
            next_left = left.next

            cur.next = left
            cur = cur.next

            left = next_left
        else:
            next_right = right.next

            cur.next = right
            cur = cur.next

            right = next_right

    if left:
        cur.next = left

    if right:
        cur.next = right

    return res.next   # Head has junk value


def mergesort(l1):
    if l1 == None or l1.next == None:
        return l1

    middle = find_middle(l1)

    second_half = middle.next
    first_half = l1
    middle.next = None

    # Divide
    left = mergesort(first_half)
    right = mergesort(second_half)

    merged_list = merge(left, right)
    return merged_list


# print_ll(merge(left, right))
# print_ll(find_middle(right))
print_ll(mergesort(l1))
