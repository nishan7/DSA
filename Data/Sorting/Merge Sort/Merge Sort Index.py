'''
#### Name:  Merge Sort
Link: [link]()

#### Sub_question_name: Merge Sort Index 
Link: [link]()

'''


def mergesort(arr, low, high):
    if low >= high:   # Require aleast 2 element 
        return 

    mid = (low + high)//2
    # low - mid     # left, inclusive
    # mid+1 - high  # right, inclusive

    mergesort(arr, low, mid)    # left
    mergesort(arr, mid+1, high) # right


    i = low
    j = mid + 1
    k = 0
    temp = [0] * (high - low +1)     # temp variable to store the merged result, O(n) space

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1

        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    
    while j <= high:
        temp[k] = arr[j]
        k += 1
        j += 1
    

    for l in range(low, high+1):
        arr[l] = temp[l - low]




arr = [12, 11, 13, 5, 6, 7]
mergesort(arr, 0, len(arr)-1)
print(arr)
