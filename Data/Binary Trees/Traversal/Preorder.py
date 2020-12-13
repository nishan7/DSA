'''
#### Name:  Traversal
Link: [link]()

#### Sub_question_name: Preorder 
Link: [link]()

'''

def preorder(root):
    if root == None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# 5 3 2 4 6



