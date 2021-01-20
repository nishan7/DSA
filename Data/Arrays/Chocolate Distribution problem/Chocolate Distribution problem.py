'''
#### Name:  Chocolate Distribution problem
Link: [link]()
Sort and Search

**O(nlogn) O(1) **
'''


def min_diff(nums, students):
    n = len(nums)
    nums.sort()

    min_value = float('inf')
    for i in range(students-1, n):
        min_value = min(min_value, nums[i] - nums[i-(students-1)])

    print(min_value)


arr = [12, 4, 7, 9, 2, 23, 25, 41,
       30, 40, 28, 42, 30, 44, 48,
       43, 50]
students = 7
min_diff(arr, students)
