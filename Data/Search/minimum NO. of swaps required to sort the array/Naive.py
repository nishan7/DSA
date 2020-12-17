'''
#### Name:  Minimum no. of swaps required to sort the array
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()

Just sort a copy of the array and compare

**O(nlogn + n^2) O(n)**
'''


def swaps(nums):
    n = len(nums)
    temp = nums.copy()
    temp.sort()

    ans = 0
    for i in range(n):
        if nums[i] != temp[i]:
            ans += 1

            idx = nums.index(temp[i])
            nums[i], nums[idx] = nums[idx], nums[i]

    print(ans)


a = [101, 758, 315, 730,
     472, 619, 460, 479]
swaps(a)
