'''
#### Name:  Find if there is any subarray with sum equal to 0
Link: [link]()

#### Sub_question_name: Print subarray indices 
Link: [link]()

Same concept as before but also store the indices

**O(N) O(N)**
'''

def zero_subarry(nums):
    n = len(nums)

    sums = {nums[0]: 0}
    for i in range(1, n):
        nums[i] = nums[i] + nums[i-1]

        if nums[i] == 0:
            print('Range {} {}'.format(0, i))

        if nums[i] in sums.keys():
            for start in sums[nums[i]]:
                print('Range {} {}'.format(start+1, i))
            sums[nums[i]].append(i)

        else:
            sums[nums[i]] = [i]


arr = [6, 3, -1, -3, 4, -2,  2, 4, 6, -12, -7]
zero_subarry(arr)
