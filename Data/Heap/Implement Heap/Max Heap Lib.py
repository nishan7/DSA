'''
#### Name:  Implement Heap
Link: [link]()

#### Sub_question_name: Max Heap Lib 
Link: [link]()

'''


from heapq import heappush, heappop, heapify

h = []
h_push = lambda item: heappush(h,-1 * item)
h_pop = lambda: -1 * heappop(h)
h_max = lambda: -1 * h[0]

h_push(5)
h_push(2)
h_push(7)
h_push(2)

print(h_pop())
print(h_pop())
print(h_pop())
print(h_pop())
