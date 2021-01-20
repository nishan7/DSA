'''
#### Name:  Flatten BST
Link: [link]()

Simply use inorder traversal to flatten BST
'''
def inorder(root, second):
    if root is None:  
        return second
    
    second = inorder(root.left, second)
    
    # Creating new node way
    # new_node = Node(root.val)
    # second.right = new_node
    # second = new_node

    # Using same node
    second.right = root
    second = root
    second.left = None  # Remove the left subtree of the array

    second = inorder(root.right, second)
    
    return second

def show(root):
    if root == None:
        return

    show(root.left)
    print(root.val, end=" ")
    show(root.right)


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


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

new_root = Node('-1')
inorder(r, new_root)
print()
show(new_root)