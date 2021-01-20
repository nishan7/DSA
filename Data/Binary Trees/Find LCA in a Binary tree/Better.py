'''
#### Name:  Find LCA in a Binary tree
Link: [link]()

#### Sub_question_name: Better 
Link: [link]()

'''



class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Program


def lca(root, n1, n2):
    if root == None:
        return False

    if root.data == n1 or root.data == n2: # We found one
        return root

    # Check n1, n2 in both the subtrees
    left_lca = lca(root.left, n1,n2)
    right_lca = lca(root.right, n1, n2)

    # Return the common root for these lca
    if left_lca and right_lca:
        return root

    return left_lca or right_lca   # left_lca if left_lca else: right_lca




print(lca(root, 4, 6).data)   # 1
print(lca(root, 4, 5).data)   # 2
