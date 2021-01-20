'''
#### Name:  Reverse LinkedList
Link: [link]()

#### Sub_question_name: Iterative 
Link: [link]()

**TC: O(n) SC: O(n)**
'''

def reverse(self):
    cur = self.head
    prev = None
    while cur:
        # Get the node right of cur
        right_of_cur = cur.next
        # Exchange the directions between cur and prev
        cur.next = prev
        
        prev = cur
        cur = right_of_cur
    return prev