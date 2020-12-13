'''
#### Name:  Construct Binary tree from Inorder and postorder traversal
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()

1) Similar to inorder + preorder
2) But change the preorder traversal and (right then left) subtree call

**O(n^2)**
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
    node = Node(postorder[len(postorder) - index-1])
    value = postorder[len(postorder) - index-1]
    index += 1

    left, right = bisect(inorder, value)
    node.right = tree(right)
    node.left = tree(left)

    return node


def postorder_t(root):
    if root == None:
        return

    postorder_t(root.left)
    postorder_t(root.right)
    print(root.data, end=' ')


inorder = 'DBEAFC'
postorder = 'ABDECF'

inorder = '48251637'
postorder = '84526731'

root = tree(postorder)
postorder_t(root)
