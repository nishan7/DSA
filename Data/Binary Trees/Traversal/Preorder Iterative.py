'''
#### Name:  Traversal
Link: [link]()

#### Sub_question_name: Preorder Iterative 
Link: [link]()

Using stack (right first append)
Pop and print
'''


def preorder(root):
    stack = []
    ans = []

    stack.append(root)

    while stack:
        curr = stack.pop()
        ans.append(curr.data)

        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)


    print(ans)

# [5, 3, 2, 4, 6]


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

#     5
#    / \        Inorder   2 3 4 5 6
#   3   6       Preorder  [5, 3, 2, 4, 6]
#  / \          Postorder 2 4 3 6 5
# 2   4


preorder(root)
