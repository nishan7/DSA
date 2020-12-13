'''
#### Name:  Diameter of a Binary Tree
Link: [link](https://www.youtube.com/watch?v=zmPj_Ee3B8c&list=PL_z_8CaSLPWfxJPz2-YKqL9gXWdgrhvdn&index=3)

Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

We need to find height for every node's subtree (So, that is repetative job)
Sum of that height(left & right subtree) is the answer


**O(n)**
'''

ans = 0

# Modified Height of Tree
def diameter(root):
    global ans
    if root == None:
        return 0

    left = diameter(root.left)
    right = diameter(root.right)

    temp = 1 + left + right

    ans = max(ans, temp)

    return 1 + max(left, right)   # We return heigh of tree


class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

root = Node()
root.left = Node()
root.right = Node()
root.left.left = Node()
root.left.right = Node()


diameter(root)
print(ans)