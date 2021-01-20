'''
#### Name:  Construct BST from preorder traversal
Link: [link]()


**O(N^2)**
'''


def create_bst(root_value, values):
    new_node = Node(root_value)

    if len(values) == 0:
        return new_node

    left_values = []
    right_values = []
    for v in values:
        if v < root_value:
            left_values.append(v)
        else:
            right_values.append(v)
    
    if left_values:
        new_node.left = create_bst(left_values[0], left_values[1:])
    
    if right_values:
        new_node.right = create_bst(right_values[0], right_values[1:])

    return new_node


## Driver
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def show(root):
    if root == None:
        return
    show(root.left)
    print(root.val, end=" ")
    show(root.right)


#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50
po = [10, 5, 1, 7, 40, 50]
r = create_bst(po[0], po[1:])
show(r)
