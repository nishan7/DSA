'''
#### Name:  Find LCA in a Binary tree
Link: [link]()

1) Get path for n1 and n2 
2) Compare and get the common path

**O(3n) **
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


def lca(root, n1, n2):
    n1_path = []
    n2_path = []
    traversal(root, n1_path, n1)
    traversal(root, n2_path, n2)
    print(n1_path)
    print(n2_path)

    i = 0
    while i < len(n1_path) and i < len(n2_path):
        if n1_path[i] != n2_path[i]:
            break
        i += 1

    print(n1_path[i-1])


lca(root, 4, 6)   # 1
lca(root, 4, 5)   # 2
