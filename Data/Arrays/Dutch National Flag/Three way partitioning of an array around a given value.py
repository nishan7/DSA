'''
#### Name:  Dutch National Flag
Link: [link]()

#### Sub_question_name: Three way partitioning of an array around a given value 
Link: [link]()

'''


def parition(nums, range):
    n = len(nums)

    low = range[0]
    high = range[1]

    start = 0
    end = n-1
    i = 0
    while i <= end:
        if nums[i] < low:  # swap with starts
            nums[start], nums[i] = nums[i], nums[start]
            i += 1
            start += 1

        elif nums[i] > high:
            nums[end], nums[i] = nums[i], nums[end]   # We donot increment i here as we many have to check for it
            end -= 1

        else:
            i += 1

    print(nums)


arr = [1, 14, 5, 20, 4, 2, 54,  20, 87, 98, 3, 1, 32]
range = (10, 20)
parition(arr, range)
