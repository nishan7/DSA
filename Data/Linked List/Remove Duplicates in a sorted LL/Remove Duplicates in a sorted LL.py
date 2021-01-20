'''
#### Name:  Remove Duplicates in a sorted LL.
Link: [link]()

'''

def removeDuplicates(head):

    cur = head.next
    prev = head
    while cur != None:
        if prev.data == cur.data:
            prev.next = cur.next
            cur = cur.next
            continue

        # prev.next = cur
        prev = cur
        cur = cur.next

    # prev.next = None 

    return head



def removeDuplicates(head):

    cur = head.next
    prev = head
    while cur != None:
        if prev.data == cur.data:
            cur = cur.next
        else:
            prev.next = cur
            cur = cur.next
            prev = prev.next

    prev.next = None  # in case of 1 2 4 4

    return head


def removeDuplicates(head):

    cur = head.next
    prev = head
    while cur != None:
        if prev.data == cur.data:
            prev.next = cur.next
            cur = cur.next
            continue

        # prev.next = cur
        prev = cur
        cur = cur.next

    # prev.next = None 

    return head
