'''
#### Name:  Largest/Smallest Subarray of Size k
Link: [link]()

Sliding window the variable window size

'''


def subarry_sum_max(arr, req_sum):
    n = len(arr)
    i = 0
    j = 0

    max_count = 0  # For min float('inf')
    window_sum = arr[0]
    while i < n and j < n:
        # window_sum += arr[j]

        if window_sum == req_sum:
            max_count = max(j-i+1, max_count)
            window_sum -= arr[i]    # We moving the window
            i += 1
            j += 1
            if j < n:
                window_sum += arr[j]

        elif window_sum < req_sum:  # Expand window
            j += 1
            if j < n:
                window_sum += arr[j]

        elif window_sum > req_sum:   # Decrease window
            window_sum -= arr[i]
            i += 1

    return max_count


def subarry_sum_min(arr, req_sum):
    n = len(arr)
    i = 0
    j = 0

    max_count = float('inf')  # For min float('inf')
    window_sum = arr[0]
    while i < n and j < n:
        # window_sum += arr[j]

        if window_sum == req_sum:
            max_count = min(j-i+1, max_count)
            window_sum -= arr[i]    # We moving the window
            i += 1
            j += 1
            if j < n:
                window_sum += arr[j]

        elif window_sum < req_sum:  # Expand window
            j += 1
            if j < n:
                window_sum += arr[j]

        elif window_sum > req_sum:   # Decrease window
            window_sum -= arr[i]
            i += 1

    return max_count


arr = [1, 3, 4, 11, 8, 1, 1, 1, 1]
req_sum = 4

arr = [51, 49, 1, 1, 6, 45, 6, 10, 19]
req_sum = 51

print(subarry_sum_max(arr, req_sum))
print(subarry_sum_min(arr, req_sum))
