'''
#### Name:  Find  Starting point of the loop.
Link: [link]()

**O(n) O(1)**
'''

def detectLoop(self): 
    slow_p = self.head 
    fast_p = self.head 
    while(slow_p and fast_p and fast_p.next): 
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p: 
            return slow_p # starting point