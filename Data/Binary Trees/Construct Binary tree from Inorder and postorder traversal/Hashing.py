'''
#### Name:  Construct Binary tree from Inorder and postorder traversal
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

**O(n) O(n)**
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


def tree(inorder, start=0):           # O(N)
    if inorder == '':
        return None

    global index
    node = Node(postorder[len(postorder) - index-1])
    value = postorder[len(postorder) - index-1]
    index += 1

    # left, right = bisect(inorder, value)
    index_of_key = postorder_table[value] - start
    node.left = tree(inorder[:index_of_key], start)
    node.right = tree(inorder[index_of_key+1:], index_of_key+1)

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

postorder_table = {}
for idx, node in enumerate(postorder):
    postorder_table[node] = idx

root = tree(inorder)
postorder_t(root)
