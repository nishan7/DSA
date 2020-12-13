'''
#### Name:  Construct Binary tree from Inorder and preorder traversal
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()


**O(N)**
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bisect(inorder, key):
    if inorder == '':
        return '', ''

    index_of_key = inorder.index(key)        # O(N)
    left = inorder[:index_of_key]        
    right = inorder[index_of_key+1:]

    return left, right


index = 0


def tree(inorder):           # O(N)
    if inorder == '':
        return None

    global index
    node = Node(preorder[index])
    value = preorder[index]
    index += 1

    left, right = bisect(inorder, value)
    node.left = tree(left)
    node.right = tree(right)

    return node


def postorder(root):
    if root == None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')


inorder = 'DBEAFC'
preorder = 'ABDECF'
root = tree(inorder)
postorder(root)
