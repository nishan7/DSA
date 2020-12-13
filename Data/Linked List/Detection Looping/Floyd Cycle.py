'''
#### Name:  Detection Looping
Link: [link]()

#### Sub_question_name: Floyd Cycle 
Link: [link]()
 
- Use 2 pointers fast and slow
- Slow pointer moves one node at a time, whereas fast moves 2 nodes at a time
- If fast and slow pointer meet then loop is detected 
- Position of slow pointer is the starting location

'''

def detectLoop(node): 
    slow = node
    fast = node
    while(slow and fast and fast.next): 
        slow = slow.next
        fast = fast.next.next
        if slow == fast: 
            return slow # starting point or return False

    return False