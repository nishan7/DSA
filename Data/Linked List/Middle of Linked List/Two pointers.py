'''
#### Name:  Middle of Linked List
Link: [link]()

#### Sub_question_name: Two pointers 
Link: [link]()

- Use 2 pointers fast and slow
- Slow pointer moves one node at a time, whereas fast moves 2 nodes at a time
- When fast pointer reaches the end, slow pointer is at middle

'''


def find_middle(node):
    fast = slow = node

    # [1,2,3]=>2, [1,2,3,4]=>3
    while fast.next != None and fast != None:
        slow = slow.next
        fast = fast.next.next

    return slow.data, slow
