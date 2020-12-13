'''
#### Name:  Implement Heap
Link: [link]()

#### Sub_question_name: Min Heap Lib 
Link: [link]()

'''

from heapq import heappush, heappop, heapify

h = []
heapify(h)

heappush(h, 5)
heappush(h, 2)
heappush(h, 1)
heappush(h, 3)
heappush(h, 0)

print(h[0])


print(heappop(h))
print(heappop(h))
print(heappop(h))