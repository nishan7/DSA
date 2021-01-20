'''
#### Name:  Check if a Binary Tree contains duplicate subtrees of size 2 or more*
Link: [link]()

Simple: Iterate a compare every node with every other  

Hashing + Serailization
'''

MARKER = '$'


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def duplicate_subtree(root, subtree=set()):
    s = ''

    if root == None:
        s = s+ MARKER

    
    # Check in left subtree
    left_str = duplicate_subtree(root.left, subtree)
    if s in left_str:
        return s
    
    # Check for right subtree
    right_subtree = duplicate_subtree(root.right, subtree)
    if s in right_subtree:
        return s
    
    s = s + root.data + left_str + right_str
