'''
#### Name:  Longest consecutive subsequence
Link: [link]()

#### Sub_question_name: Sorting 
Link: [link]()

 Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, 
 the consecutive numbers can be in **any order**.

Sort and count
**O(nlogn + n) O(nlogn)**
'''


def lcs(nums):
    nums.sort()

    ctr = 1
    ans = 0
    for i in range(1, len(nums)):
        if nums[i-1] + 1 == nums[i]:
            ctr += 1
            ans = max(ans, ctr)
        else:
            ctr = 1

    print(ans)


nums = [5, 3, 2,  8, 1, 4]
lcs(nums)
