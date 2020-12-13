'''
#### Name:  Check if Binary tree is Sum tree or NOT
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()

**O(n^2) for skewed tree**
'''


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_sum(root):
    if root == None:
        return 0

    return root.data + tree_sum(root.left) + tree_sum(root.right)


def is_sum_tree(root):
    if root == None or (root.left == None and root.right == None):
        return True

    if root.data == tree_sum(root.left) + tree_sum(root.right) and is_sum_tree(root.left) and is_sum_tree(root.right):
        return True

    return False


root = node(26)
root.left = node(10)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(6)
root.right.right = node(3)

print(is_sum_tree(root))
