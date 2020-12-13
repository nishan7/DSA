'''
#### Name:  Mirror of Tree
Link: [link]()

Level order only
'''

def mirror( root ):
    if root == None:
        return 0
    
    stack = []
    stack.append(root)

    while stack:
        current = stack.pop()
        print(current.data, end=" ")

        if current.right:
            stack.append(current.right)
        
        if current.left:
            stack.append(current.left)

# 5 3 2 4 6


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

#   5
#  / \
# 6   3
#    / \
#   4   2

print ("Level Order Traversal of binary tree is -")
print(mirror(root))

