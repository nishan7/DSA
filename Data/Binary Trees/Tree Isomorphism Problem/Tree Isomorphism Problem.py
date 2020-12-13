'''
#### Name:  Tree Isomorphism Problem
Link: [link]()

**O(min(m,n)*2)**
'''


class Node:
    # Constructor to create the node of binary tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)

n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right = Node(7)


# program

# Bases on principle for every node their children should match (ll & rr or lr & lr )
def is_iso(r1, r2):
    if r1 is None and r2 is None:
        return True

    if r1 is None or r2 is None:
        return False

    if r1.data != r2.data:
        return False

    return (is_iso(r1.left, r2.left) and is_iso(r1.right, r2.right)) or (is_iso(r1.left, r2.right) and is_iso(r1.right, r2.left))


print(is_iso(n1, n2))
