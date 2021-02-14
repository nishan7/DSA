'''
#### Name:  Rotate a Array by k
Link: [link]()

#### Sub_question_name: Inplace Reverse 
Link: [link]()

example:

Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
'''


def reverse(nums, start, end):
    for i in range((end-start)//2):
        nums[start+i], nums[end-i-1] = nums[end-i-1], nums[start+i]
    # while start < end:
    #     nums[start], nums[end] = nums[end], nums[start]
    #     start, end = start + 1, end - 1


def rotate(nums, k):
    n = len(nums)
    k = k % n

    reverse(nums, 0, n)
    reverse(nums, 0, k)
    reverse(nums, k, n)
    print()


nums = [1, 2, 3, 4, 5, 6]
k = 2


rotate(nums, k)
print(nums)
