'''
#### Name:  Find distance between 2 Nodes in a Binary tree
Link: [link]()

Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca) 
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


def traversal(root, path, key):
    if root == None:
        return False

    path.append(root.data)

    if root.data == key:
        return True

    if traversal(root.left, path, key) or traversal(root.right, path, key):
        return True

    path.pop()


def diff(root, n1, n2):
    path_n1 = []
    traversal(root, path_n1, n1)
    path_n2 = []
    traversal(root, path_n2, n2)

    for i in range(len(path_n1)):
        if path_n1[i] != path_n2[i]:
            break

    lca = path_n1[i-1]
    print(lca)

    path_lca = []
    traversal(root, path_lca, lca)
    print(path_n1, path_n2, path_lca)

    print(len(path_n1) + len(path_n2) - 2*len(path_lca))


diff(root, 4, 5)   #
