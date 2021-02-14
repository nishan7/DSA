'''
#### Name:  Rotate a Array by k
Link: [leetcode](https://leetcode.com/problems/rotate-array/solution/)

#### Sub_question_name: Inplace Swap 
Link: [link]()

It will form a graph which has n number of edges
'''

def rotate(nums, k):
    n = len(nums)
    k = k % n

    counter = 0
    start = 0
    while counter < n:   
        current, prev = start, nums[start]
        while True:
            next_index = (current + k) % n
            prev, nums[next_index] = nums[next_index], prev

            counter += 1
            current = next_index
            if current == start:
                break
        start += 1






nums=[1, 2, 3, 4, 5, 6]
k= 2


rotate(nums, k)
print(nums)