'''
#### Name:  Check Binary Tree
Link: [link]()

#### Sub_question_name: Optimal 
Link: [link]()

Use the program for height
And global variable to keep track of fail condition 
'''

res = True
def is_balanced(root):
    global res
    if root == None:
        return 0
    
    left = is_balanced(root.left)
    right = is_balanced(root.right)

    res = res and (abs(left-right) < 2)
    
    return 1 + max(left, right)



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
print(res)