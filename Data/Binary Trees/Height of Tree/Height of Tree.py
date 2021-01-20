'''
#### Name:  Height of Tree
Link: [link]()

**TC: O(n)** n is number of node in the tree
'''

def height( root ):
    if root == None:
        return 0
    
    return max(1+ height(root.left), 1 + height(root.right))



class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
 

#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
print(height(root))   # [1, 3, 2, 5, 4]