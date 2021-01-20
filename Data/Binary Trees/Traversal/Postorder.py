'''
#### Name:  Traversal
Link: [link]()

#### Sub_question_name: Postorder 
Link: [link]()

'''

def postorder(root):
    if root == None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
    

# 2 4 3 6 5

