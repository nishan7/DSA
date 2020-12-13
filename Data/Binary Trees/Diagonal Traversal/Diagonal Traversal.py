'''
#### Name:  Diagonal Traversal
Link: [link]()

Maintain a queue and stack
'''
def traverse(root):
    
    queue = []
    stack = []
    ans = []

    stack.append(root)

    while stack or queue:

        if len(stack) == 0:
            stack.append(queue.pop(0))  # Move a element from queue to stack
        
        curr = stack.pop()
        ans.append(curr.data)

        if curr.left:
            queue.append(curr.left)
        
        if curr.right:
            stack.append(curr.right)
        

    print(ans)

#[5, 6, 3, 4, 2]

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
traverse(root)

#     5           LR
#    / \
#   3   6         RL
#  / \
# 2   4           LR

