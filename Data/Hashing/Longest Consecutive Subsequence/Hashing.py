'''
#### Name:  Longest consecutive subsequence
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

Use a set to track numbers

**O(n) O(n)**
'''


def lcs(nums):
    numbers_set = set(nums)
    res = 0
    for number in nums:

        if number-1 not in numbers_set:  # making sure only to choose starting elements
            j = number

            while j in numbers_set:
                j += 1

            res = max(res, j - number)

    print(res)


nums = [5, 3, 2, 8, 1, 4]
lcs(nums)
