'''
#### Name:  Convert Binary Tree to Doubly Linked List
Link: [link]()


1) Do a inorder traversal 
2) Create a DLL based on that traversal
'''


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder(root, res):
    if root == None:
        return
    inorder(root.left, res)
    res.append(root)
    inorder(root.right, res)


def to_dll(root):
    res = []
    inorder(root, res)
    print([n.data for n in res])
    head = res[0]
    head.left = None
    prev = head
    for node in res[1:]:
        prev.right = node
        node.left = prev
        prev = node

    print(head.right.right.data)


root = Node(1)
root.right = Node(2)
root.left = Node(3)


to_dll(root)
