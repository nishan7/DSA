'''
#### Name:  Print all "K" Sum paths in a Binary tree
Link: [link]()

1) Preorder keeping tracks

**O(n^2)**
'''


class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


root = newNode(1)
root.left = newNode(3)
root.left.left = newNode(2)
root.left.right = newNode(1)
root.left.right.left = newNode(1)
root.right = newNode(-1)
root.right.left = newNode(4)
root.right.left.left = newNode(1)
root.right.left.right = newNode(2)
root.right.right = newNode(5)
root.right.right.right = newNode(2)


# Code
def k_sum(root, k, path):
    if root == None:
        return
    
    path.append(root.data)
    k_sum(root.left, k, path)
    k_sum(root.right, k, path)

    # At the leaf node
    summer = 0
    for idx, node_value in enumerate(reversed(path)):
        summer += node_value
        
        if summer == k: # We got the path, desired way is starts form (idx+1) position from the back
            print(path[-(idx+1):])

    # Remove the current element form the path
    path.pop()  # Like removing the leaf node  because we are going up


        

k = 5
k_sum(root, k, [])
