'''
#### Name:  Identification
Link: [link]()

#General Syntax
'''

def func (root):

    # BASE COND
    if root == None:
        return 0

    # HYPOTHESIS
    l = solve(root.left)
    r = solve(root.right)

    # INDUCTION 