'''
#### Name:  Find min and max value in a BST
Link: [link]()

'''


def min_val(root):
    if root.left == None:
        return root.val

    return min_val(root.left)  # First case for when there is singe root


def max_val(root):
    if root.right == None:
        return root.val

    return max_val(root.right)  # First case for when there is singe root


print(max_val(r))   # 80
print(min_val(r))   # 20
#     50
#   /     \
#  30     70
#  / \    / \
# 20 40  60 80
