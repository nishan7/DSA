'''
#### Name:  Find LCA  of 2 Nodes in a BST
Link: [link]()

Just compare both values with root. 
If there is split from that root, then thats the answer
'''
def lca(root, val1, val2):
    if val1 < root.val and val2 < root.val:
        return lca(root.left, val1, val2)

    elif val1 > root.val and val2 > root.val:
        return lca(root.right, val1, val2)

    return root.val



## Driver
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

print(lca(r, 40, 60))
print(lca(r, 60, 60))
print(lca(r, 40, 70))
