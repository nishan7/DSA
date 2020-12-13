'''
#### Name:  Diameter of Tree
Link: [link]()

Diameter is the at the point where height(left subtree) + height(right subtree) is max

**O(n)**

'''


def diameter(root, max_diameter=0):
    if root == None:
        return 0

    max_diameter = max(max_diameter, 1+diameter(root.left,
                                                max_diameter)+diameter(root.right, max_diameter))

    return max_diameter


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
print(diameter(root))   # [1, 3, 2, 5, 4]
