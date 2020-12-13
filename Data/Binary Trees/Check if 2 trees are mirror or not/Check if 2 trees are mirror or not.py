'''
#### Name:  Check if 2 trees are mirror or not
Link: [link]()

Just recurisvely check for (left -right) (right-left) subtree of the tree
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root1 = Node(1) 
root2 = Node(1) 
  
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(3) 
root2.right = Node(2) 
root2.right.left = Node(5) 
root2.right.right = Node(4) 


# program

def are_mirror(r1, r2):
    if r1 is None and r2 is None:
        return True
    
    if r1 is None or r2 is None:
        return False
    
    return r1.data == r2.data and are_mirror(r1.left, r2.right) and are_mirror(r1.left, r2.right)


print(are_mirror(root1, root2))