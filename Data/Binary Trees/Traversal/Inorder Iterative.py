'''
#### Name:  Traversal
Link: [link]()

#### Sub_question_name: Inorder Iterative 
Link: [link]()

'''
def inorder(root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:        # No more nodes to left
            curr = stack.pop()          # Get the latest mid value
            print(curr.data, end=" ")   # print it
            curr = curr.right           # go right 


def inorder(root):
    stack = []
    stack.appned(root)

    while stack:
        tos = stack[-1]
        if tos.left:
            stack.append(tos.left)
        else:                     # No more nodes to left
            tos = stack.pop()          # Get the latest mid value
            print(tos.data, end=" ")   # print it
            stack.append(tos.right)           # go right 

# 2 3 4 5 6

