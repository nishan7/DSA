'''
#### Name:  Minimum no. of swaps required to sort the array
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

We can optimize the index  operation by using dictionary

**O(nlogn + n) O(n)**
'''


def swaps(nums):
    n = len(nums)
    temp = nums.copy()
    temp.sort()

    index = {nums[i]: i for i in range(n)}
    print(index)
    ans = 0
    for i in range(n):
        if nums[i] != temp[i]:
            ans += 1

            # idx = nums.index(temp[i])
            idx = index[temp[i]]
            
            # Also make changes in dictionary too!
            index[nums[i]] = idx
            index[nums[idx]] = i
            
            # Swaps
            nums[i], nums[idx] = nums[idx], nums[i]

    print(ans)


a = [101, 758, 315, 730,
     472, 619, 460, 479]
swaps(a)
