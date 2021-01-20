'''
#### Name:  Reverse Level Order Traversal
Link: [link]()

#### Sub_question_name: Better 
Link: [link]()

Same as level order but store the results in a queue(insert first)
'''

def reverseOrder(root):
    queue = []  # Stores traversal
    res = []  # Stores ans

    queue.append(root)

    while queue:
        current = queue.pop(0)
        # print(current.data)
        res.insert(0, current.data)

        left = current.left
        right = current.right

        if right:
            queue.append(right)

        if left:
            queue.append(left)


    return res

# [4, 5, 2, 3, 1]

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
 
root = Node(5)                  # [2, 4, 9, 3, 6, 5]
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(9)  


#     5
#    /  \        Inorder   2 3 4 5 6
#   3    6       Preorder
#  / \    \       Postorder 2 4 3 6 5
# 2   4    9

print("Level Order Traversal of binary tree is -")
print(reverseOrder(root))   # [4, 5, 2, 3, 1]
