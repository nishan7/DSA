'''
#### Name:  Traversal
Link: [link]()

#### Sub_question_name: Inorder 
Link: [link]()

'''
def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

# 2 3 4 5 6

class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
 

#Driver Program to test above function
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)

#     5
#    / \        Inorder   2 3 4 5 6
#   3   6       Preorder  
#  / \          Postorder 
# 2   4

print ("Level Order Traversal of binary tree is -")
inorder(root)

