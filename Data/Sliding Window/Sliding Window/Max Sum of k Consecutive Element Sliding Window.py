'''
#### Name:  Sliding Window
Link: [link]()

#### Sub_question_name: Max Sum of k Consecutive Element Sliding Window 
Link: [link]()

'''


def subarray_sum(arr, k):
    n = len(arr)
    i = 0
    j = 0

    min_sum = float('inf')
    window_sum = arr[0]
    while j < n:
        if j-i+1 < k:  # If our window is small increase it
            j += 1
            window_sum += arr[j]

        else:       # Size of window is ok; move our windows; find maximum sum
            min_sum = min(min_sum, window_sum)
            window_sum = window_sum - arr[i] + arr[j]
            i += 1
            j += 1

    return min_sum


arr = [1, 3, 4, 11, 8, 2]
k = 3
print(subarray_sum(arr, k))

# Min => 8 Max= 23;
