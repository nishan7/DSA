'''
#### Name:  Largest sum contiguous Subarray
Link: [link]()

We iterate and find sum of the array elements so far.
Keep track of max_sum variable and put max elemnt from sum_so_far

**O(n)**
'''
# Normal Kadane's
def contigous_sum(arr):
    n = len(arr)

    max_sum = 0
    sum_so_far = 0

    for num in arr:
        sum_so_far = max(0, sum_so_far+num)
        max_sum = max(max_sum, sum_so_far)

    return max_sum



arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(contigous_sum(arr))

# Negative inclusive Kadane's
def contigous_sum(arr):
    n = len(arr)

    max_sum = arr[0]    # Initalize with first element
    sum_so_far = arr[0] 

    for num in arr[1:]:
        sum_so_far = max(num, sum_so_far+num)   # Set the max value for current element
        max_sum = max(max_sum, sum_so_far)

    return max_sum



arr = [-2, -3, -4, -2, -5, -3]
print(contigous_sum(arr))



# Printing index Kadane's
def contigous_sum(arr):
    n = len(arr)
    sum = 0
    range = ()
    max_sum = 0
    sum_so_far = 0

    for idx, num in enumerate(arr):
        # sum_so_far = max(0, sum_so_far+num)
        if sum_so_far + num > sum_so_far:
            sum_so_far = sum_so_far + num
        else:
            sum_so_far = 0
            start = idx+1       # Keeping track of starting point of array, it will start in next index after it resets

        # max_sum = max(max_sum, sum_so_far)
        if sum_so_far > max_sum:
            max_sum = sum_so_far         
            range = (start, idx)  # Keep actual range track, start to idx
        
    # max_sum = 0 => Answer not found
    print(max_sum, arr[range[0]:range[1]+1])



arr = [-2, -3, 4, -1, -2, 1, 5, -3]
contigous_sum(arr)