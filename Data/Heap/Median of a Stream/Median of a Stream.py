'''
#### Name:  Median of a Stream
Link: [link]()

1) Use 2 heaps 
2) MIN HEAP to store numbers greater than median
3) MAX_HEAP to store nubmers less than median
4) Both heaps can have difference of 1 or 0
5) if difference is 1 print from the heap having greater number
6) if difference is 0 print average from 2 numbers


'''

from heapq import heappush, heappop

min_heap_ds = []
max_heap_ds = []


# MIN Heap for elements greater than med
def greater_push(x): return heappush(min_heap_ds, x)


def greater_pop(): return heappop(min_heap_ds)


def greater_peek(): return min_heap_ds[0]


def greater_size(): return len(min_heap_ds)

# MAX Heap for elements smaller than med


def smaller_push(x): return heappush(max_heap_ds, -1 * x)


def smaller_pop(): return -1 * heappop(max_heap_ds)


def smaller_peek(): return -1 * max_heap_ds[0]


def smaller_size(): return len(max_heap_ds)


def median(nums):
    med = nums[0]
    print(med)
    ans = []
    ans.append(med)
    smaller_push(med)

    for number in nums[1:]:

        if greater_size() == smaller_size():  # Both heaps are balanced
            if number > med:
                greater_push(number)
                med = greater_peek()
            else:
                smaller_push(number)
                med = smaller_peek()

        elif greater_size() > smaller_size():
            if number > med:    # Self item from greater_heap to smaller_heap
                smaller_push(greater_pop())
                greater_push(number)
            else:
                smaller_push(number)

            med = (smaller_peek() + greater_peek())/2

        elif greater_size() < smaller_size():
            if number > med:
                greater_push(number)
            else:
                greater_push(smaller_pop())
                smaller_push(number)
            med = (smaller_peek() + greater_peek())/2
        print(med)
        ans.append(med)
    return med


nums = [5, 15, 10, 20, 3]   # 5, 10,10,12.5,10
nums = [5, 15, 1,3,2,8,7,9,10,6,11,4]
median(nums)
