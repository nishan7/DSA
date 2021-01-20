'''
#### Name:  Zigzag Traversal
Link: [link]()

'''


def zigzag(root):
    queue = []
    queue.append(root)

    res = []

    level = -1
    while queue:
        n = len(queue)  # Number of node in a level

        level_res = []  # Every level has a result
        level += 1
        for i in range(n):
            curr = queue.pop(0)

            if level % 2 == 0:  # LR
                level_res.append(curr.data)
            elif level % 2 == 1:  # RL
                level_res.insert(0, curr.data)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        res = res + level_res
    print(res)

# [5, 6, 3, 2, 4]

class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0


# Driver Program to test above function
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)

#     5           LR
#    / \
#   3   6         RL
#  / \
# 2   4           LR


zigzag(root)
