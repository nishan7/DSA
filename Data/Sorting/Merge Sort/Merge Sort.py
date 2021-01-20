'''
#### Name:  Merge Sort
Link: [link]()


**O(nlogn) || SC: O(n) || not inplace || stable ||**
'''

# Python program for implementation of MergeSort

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        # merge left and right array to arr
        i = j = k = 0
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1
        
        while len(left) > i: # arr = 
            arr[k] = left[i] 
            i += 1 
            k += 1
        
        while len(right) > j:
            arr[k] = right[j]
            j += 1
            k += 1
        
        ## arr = left[i:]+right[j:]




arr = [12, 11, 13, 5, 6, 7]
mergesort(arr)
print(arr)