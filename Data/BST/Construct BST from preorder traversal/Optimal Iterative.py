'''
#### Name:  Construct BST from preorder traversal
Link: [link]()

#### Sub_question_name: Optimal Iterative 
Link: [link]()

'''



def create_bst(values):
    
    stack = []
    root = Node(values[0])
    stack.append(root)

    curr = root
    for v in values[1:]:
        temp = None

        while len(stack) > 0 and v > stack[-1].val: # find the place to place right val
            temp = stack.pop()

        if temp:    # Found a place
            temp.right = Node(v)
            stack.append(temp.right)

        else:       # Didn't find the place
            temp = stack[-1]
            temp.left = Node(v)
            stack.append(temp.left)
    
    return root

    


## Driver
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def show(root):
    if root == None:
        return
    show(root.left)
    print(root.val, end=" ")
    show(root.right)


#      10
#    /   \
#   5     40
#  /  \      \
# 1    7      50
po = [10, 5, 1, 7, 40, 50]
r = create_bst(po)
show(r)
