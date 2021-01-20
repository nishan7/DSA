'''
#### Name:  Reverse Level Order Traversal
Link: [link]()

# Not level order
**O(n) O(n)**

Implemented using stack and queues

'''


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def levelOrder(root):
    stack = []  # Stores traversal
    queue = []  # Stores ans

    stack.append(root)

    while stack:
        current = stack.pop()
        # print(current.data)
        queue.insert(0, current.data)

        left = current.left
        right = current.right

        if left:
            stack.append(left)

        if right:
            stack.append(right)
    return queue

    # return res
# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(9)


print("Level Order Traversal of binary tree is -")
print(levelOrder(root))   # [4, 5, 2, 3, 1]
