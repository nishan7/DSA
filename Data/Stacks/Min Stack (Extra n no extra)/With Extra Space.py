'''
#### Name:  Min Stack (Extra n no extra)
Link: [link]()

#### Sub_question_name: With Extra Space 
Link: [link]()

'''

stack = []
ss = []

def push(item):
    stack.append(item)
    
    if len(ss) == 0 or ss[-1] > item:  # if ss is empty or has element greater, than change tos
        ss.append(item)

def pop():
    popped_elem = stack.pop()
    if ss[-1] == popped_elem:
        ss.pop()
    
    return popped_elem

def get_min():
    return ss[-1]


push(5)
push(7)
print(get_min())
print(pop())
push(1)
push(11)
print(get_min())



