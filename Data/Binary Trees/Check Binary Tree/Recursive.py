'''
#### Name:  Check Binary Tree
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

'''
def height(root):
    if root == None:
        return 0
    
    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):
    left = height(root.left)
    right = height(root.right)
    # print(left, right)

    return abs(left-right) < 2



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

print(is_balanced(root))