'''
#### Name:  Check if all leaf NOdes are at same level or NOt
Link: [link]()
1) Same as step wise level order
2) Use 2 ^ (n-1) to detetermin no of leaves
'''


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    # return res
# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def levelOrder(root):
    queue = []

    queue.append(root)
    res = []
    level_ctr = 0  # Count the number of levels in the tree

    while queue:
        n = len(queue)
        level_ctr += 1

        level_nodes = []    # Store node for every level
        for i in range(n):   # Iterate level by level
            current = queue.pop()
            # print(current.data)
            level_nodes.append(current.data)

            left = current.left
            right = current.right

            if left:
                queue.append(left)

            if right:
                queue.append(right)

        res += level_nodes

    # print(level_nodes, level_ctr)

    # level = n must have 2 ^(n-1) nodes, level 0=>1 , 1=> 2, 3 => 4 ,
    if len(level_nodes) == 2 ** (level_ctr - 1):
        return True
    else:
        return False

    # return res




print("Level Order Traversal of binary tree is -")
print(levelOrder(root))   # True
