'''
#### Name:  Height of Binary Tree
Link: [link](https://www.youtube.com/watch?v=aqLTbtWh40E&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=5)


'''

def height(root):
    if root == None:
        return 0

    h1 = height(root.left)
    h2 = height(root.right)

    return 1+max(h1, h2)

class Node:
    left = None
    right = None

f = Node()
k = Node()
f.left = None
k.left = f


print(height(f))