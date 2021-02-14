'''
#### Name:  Sorted Array to BST
Link: [link]()

'''


def create_bst(nums, start, end):
    if (end - start) < 0: # or start > end
        return None

    midpoint = (start+end)//2

    root = Node(nums[midpoint])
    root.left = create_bst(nums, start, midpoint-1)
    root.right = create_bst(nums, midpoint+1, end)

    return root


def preorder(root):
    if not root:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


nums = [-10, -3, 0, 5, 9]
nums = [1, 2, 3, 4, 5, 6, 7] 
tree = create_bst(nums, 0 , len(nums)-1)
preorder(tree)
