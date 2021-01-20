'''
#### Name:  Check if a tree is a BST or Not
Link: [link]()

**Brute** Brute will be to find max value from subtree for every node

**O(n) O(n) [for res]**
'''


def check(root, res=[]):
    if root is None:
        return True

    if len(res) and res[-1] > root.val:
        return False

    left = check(root.left, res)
    res.append(root.val)
    right = check(root.right, res)

    return left and right


# class Node:
# def insert(root, value):
#     50
#   /     \
#  30     70
#  / \    / \
# 20 40  60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

r.right.right.val = 5

print(check(r))
