'''
#### Name:  Traversal
Link: [link]()

#### Sub_question_name: Postorder Iterative 
Link: [link]()



'''


def postorder(root):
    stack = []
    ans = []

    stack.append(root)

    while stack:
        curr = stack.pop()
        ans.insert(0, curr.data)

        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)

    print(ans)

# [2, 4, 3, 9, 6, 5]


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Driver Program to test above function
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(9)

#     5
#    /  \        Inorder   2 3 4 5 6
#   3    6       Preorder
#  / \    \       Postorder 2 4 3 9 6 5
# 2   4    9


postorder(root)
