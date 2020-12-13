'''
#### Name:  Find all Duplicate subtrees in a Binary tree*
Link: [link]()

Do inorder traversal and hash every subtree

'''

class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

root = None
root = newNode(1)  
root.left = newNode(2)  
root.right = newNode(3)  
root.left.left = newNode(4)  
root.right.left = newNode(2)  
root.right.left.left = newNode(4)  
root.right.right = newNode(4)  

# Program

def print_dups(root, subtrees):
    if root is None:
        return ''

    line = '(' + print_dups(root.left, subtrees) + str(root.data) + print_dups(root.right, subtrees) + ')'

    if line in subtrees:
        print(line, end=' ')
    else:
        subtrees.add(line)
    
    return line
    

subtrees = set()
print(print_dups(root, subtrees))
print(subtrees)