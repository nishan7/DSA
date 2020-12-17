'''
#### Name:  Implement
Link: [progamiz](https://www.programiz.com/dsa/binary-search-tree)

'''


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def insert(root, value):
    if root == None:
        return Node(value)

    if root == value:
        return root

    if value > root.val:
        root.right = insert(root.right, value)  # Greater -> right
    else:
        root.left = insert(root.left, value)   # Smaller or equal -> left

    return root  # if we don't return above line will just root.left = None


def show(root):
    if root == None:
        return

    show(root.left)
    print(root.val, end=" ")
    show(root.right)


def search(r, key):
    if r == None:
        return False
    elif r.val == key:
        return True

    if key > r.val:
        return search(r.right, key)
    else:
        return search(r.left, key)


def min_val(root):
    cur = root
    while cur.left:
        cur = cur.left
    return cur


def delete(root, key):
    if root == None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp

        # Get min value of right sub-tree
        temp = min_val(root.right)
        root.val = temp.val

        # Delete that node, temp
        root.right = delete(root.right, temp.val)
    return root

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
show(r)
print(search(r, 80))
delete(r, 60)
show(r)




