'''
#### Name:  Views of Tree
Link: [link]()

#### Sub_question_name: Top View 
Link: [link]()


1) Chang Node to include a horizontal distance
2) Assign hd to every node during level order traversal
3) Using a dict to keep track of all the hd and print them

**O(n) O(n)**

'''


def top_view(root):
    queue = []
    queue.append(root)
    horizontal_distance = {}

    while queue:
        curr = queue.pop(0)

        if curr.hd not in horizontal_distance:  # if this hd is not visited yet
            horizontal_distance[curr.hd] = curr.data
        else:
            horizontal_distance[curr.hd] = curr.data

        if curr.left:
            queue.append(curr.left)
            curr.left.hd = curr.hd - 1  # Update the hd of nodes

        if curr.right:
            queue.append(curr.right)
            curr.right.hd = curr.hd + 1
    
    for i in sorted(horizontal_distance.keys()):
        print(horizontal_distance[i] , end=" ")
    
    print()


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0


# Driver Program to test above function
root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)

#     5
#    / \        
#   3   6       
#  / \          
# 2   4


top_view(root)
