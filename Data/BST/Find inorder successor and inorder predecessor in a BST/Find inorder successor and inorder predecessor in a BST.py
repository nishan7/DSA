'''
#### Name:  Find inorder successor and inorder predecessor in a BST
Link: [link]()


Use inorder traversal to get predecessor or successor

'''
def inorder(root, res):
    if root is None:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

def s_p(root, key):
    inorder_res = []
    inorder(root, inorder_res)
    print(inorder_res)

    key_idx = inorder_res.index(key)   # Use binary search
    print(inorder_res[key_idx-1], inorder_res[key_idx+1])





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

key = 70
s_p(r, key)  # 60 80