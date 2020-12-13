'''
#### Name:  Detect Loop in LL
Link: [link]()

#### Sub_question_name: Sets (Hashing) 
Link: [link]()

'''
def detectLoop(head):
    #code here
    visited = set()
    cur = head
    while cur != None:
        if cur in visited:
            return False
        
        visited.add(cur)
        cur = cur.next
    return False
