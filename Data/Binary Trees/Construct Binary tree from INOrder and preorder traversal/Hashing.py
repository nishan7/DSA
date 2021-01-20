'''
#### Name:  Construct Binary tree from Inorder and preorder traversal
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

Now we hash inorder to do search in O(1)

**O(n) O(n)**
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



index = 0
def tree(inorder, start = 0):           # O(N), start is used to use inorder_table with decreasing preorder string
    if inorder == '':
        return None

    global index
    node = Node(preorder[index])
    value = preorder[index]
    index += 1

    # left, right = bisect(inorder, value)
    index_of_key = inorder_table[value] - start # Find the index of value in inorder_table
    node.left = tree(inorder[:index_of_key], start)
    node.right = tree(inorder[index_of_key+1:], index_of_key+1)

    return node


def postorder(root):
    if root == None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')



inorder = 'DBEAFC'
preorder = 'ABDECF'

inorder_table = {}
for idx, value in enumerate(inorder):
    inorder_table[value] = idx

root = tree(inorder)
postorder(root)
