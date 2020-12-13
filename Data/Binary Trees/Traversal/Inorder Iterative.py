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




# 2 3 4 5 6

