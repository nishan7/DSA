'''
#### Name:  Maximum Sum of Nodes in Binary tree such that NO two are adjacent
Link: [link]()

#### Sub_question_name: Pairs 
Link: [link]()

1) We can either choose (current + grandchildren) or children
'''


class newNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = newNode(10)
root.left = newNode(1)
root.left.left = newNode(2)
root.left.left.left = newNode(1)
root.left.right = newNode(3)
root.left.right.left = newNode(4)
root.left.right.right = newNode(5)


# program

def max_sum(root):
    if root == None:
        return [0, 0]   # current_sum, childern sum

    left = max_sum(root.left)
    right = max_sum(root.right)

    res_sum = [0, 0]

    # Current sum(root.data) with grandchildrens(left[1], right[1]) sums
    res_sum[0] = left[1] + right[1] + root.data

    # Children sum, choose children or grandchildren
    res_sum[1] = max(left[0], left[1]) + max(right[0], right[1])

    return res_sum


print(max(max_sum(root)))
