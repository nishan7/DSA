'''
#### Name:  Kth Ancestor of Node in a Binary tree
Link: [link]()

**O(n) O(n)**
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
def traversal(root, path, key):
    if root == None:
        return False

    path.append(root.data)

    if root.data == key:
        return True

    if traversal(root.left, path, key) or traversal(root.right, path, key):
        return True

    path.pop()


path = []
traversal(root, path, 2)
k = 2
# if out of bounds print -1
print(path[-k-1])  # 2+1 from behind
