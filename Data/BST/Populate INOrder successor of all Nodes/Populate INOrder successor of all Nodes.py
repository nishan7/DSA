'''
#### Name:  Populate INOrder successor of all Nodes
Link: [link]()


Reverse inorder traversal with prev value
'''

# Reverse inorder traversal
def populate(root, prev=-1):
    if root is None:  
        return prev
    
    prev = populate(root.right, prev)

    root.next = prev
    prev = root.val  # Successor for smaller value

    prev = populate(root.left, prev)

    return prev
    
    
    return second

def show(root):
    if root == None:
        return

    show(root.right)
    print((root.val, root.next), end=" ")
    show(root.left)
    


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.next = None

def insert(root, value):
    if root == None:
        return Node(value)

    if root == value:
        return root

    if value > root.val:
        root.right = insert(root.right, value)  # Greater -> right
    else:
        root.left = insert(root.left, value)   # Smaller or equal -> left

    return root  # if we don't return above line will just root.left = None

#     50
#   /     \
#  30     70
#  / \    / \
# 20 40  60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

populate(r)
show(r)