'''
#### Name:  Mirror of Tree
Link: [leetcode](https://leetcode.com/problems/invert-binary-tree/solution/)

#### Sub_question_name: Recursive 
Link: [link]()

'''

class Solution:
    def invertTree(self, root):
        if root == None:
            return 
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
    
        return root