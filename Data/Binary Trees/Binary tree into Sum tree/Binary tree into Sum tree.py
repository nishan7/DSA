'''
#### Name:  Binary tree into Sum tree
Link: [link]()

'''


def sum_tree(node):
    if node == None:
        return 0

    old_val = node.val

    node.val = sum_tree(node.left) + sum_tree(node.right)

    return old_val + node.val

def printInorder(Node) : 
    if (Node == None) : 
        return
    printInorder(Node.left)  
    print(Node.val, end = " ")  
    printInorder(Node.right) 

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# Driver Program to test above function
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(9)

#     5
#    /  \        Inorder   2 3 4 5 6
#   3    6       Preorder
#  / \    \       Postorder 2 4 3 6 5
# 2   4    9


sum_tree(root)
printInorder(root)
