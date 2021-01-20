'''
#### Name:  Views of Tree
Link: [link]()

#### Sub_question_name: Right View 
Link: [link]()

Same as level order traversal, but only print last element in level order traversal
'''
# [5, 3, 2]

def right_view(root):
    queue = []
    queue.append(root)
    
    res = []
    while queue:
        n = len(queue) # To track the levels

        for i in range(n):
            curr = queue.pop(0)

            if i == n-1:               # Only for the last element in level print; [5  3,6  2,4]
                res.append(curr.data)
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)

    return res


# [5, 6, 4]