'''
#### Name:  Diameter of Tree
Link: [link]()

Diameter is the at the point where height(left subtree) + height(right subtree) is max

Calculated similar as to calcuating height but keeping track of diameter at every time

**O(n)**

'''


def height(root, max_diameter):
    if root == None:
        return 0

    left_height = height(root.left, max_diameter)
    right_height = height(root.right, max_diameter)

    max_diameter[0] = max(max_diameter[0], 1 + left_height + right_height)

    return 1 + max(left_height, right_height)


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


max_diameter = [-1]
height(root, max_diameter)  
print(max_diameter[0])  # 4