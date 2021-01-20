'''
# Name:  Detection Looping
Link: [link]()

# Sub_question_name: Sets
Link: [link]()

'''
def detectLoop(node):
    s = set()
    temp = node
    while (temp):
        if (temp in s):
            return True
        s.add(temp)
        temp = temp.next

    return False
