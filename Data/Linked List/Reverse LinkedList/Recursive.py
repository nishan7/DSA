'''
#### Name:  Reverse LinkedList
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

draw a graph and try out
**TC: O(n) SC: O(n)**
'''

def _reverse(self, cur, prev=None):
    if cur == None:
        return prev
    next_node = cur.next
    cur.next = prev
    return self._reverse(next_node, cur)