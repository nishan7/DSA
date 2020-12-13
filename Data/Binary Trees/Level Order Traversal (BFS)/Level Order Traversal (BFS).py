'''
#### Name:  Level Order Traversal (BFS)
Link: [link]()

**O(n) O(n)**
'''
class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
 

def levelOrder( root ):
    queue = []
    
    queue.append(root)
    res = []
    
    while queue:
        current = queue.pop()
        # print(current.data)
        res.append(current.data)
        
        left = current.left
        right = current.right
        
        if left:
            queue.append(left)
        
        if right:
            queue.append(right)
    return res
        
    # return res
#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
print(levelOrder(root))   # [1, 3, 2, 5, 4]