'''
#### Name:  Count Inversion
Link: [link]()

#### Sub_question_name: Optimal (Merge sort) 
Link: [gfg](https://www.geeksforgeeks.org/counting-inversions/)

**O(nlogn) O(n)**
'''

def mergesort(arr):
    if len(arr) <= 1:
        return 0
    
    count = 0

    mid  =  len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    count += mergesort(left)
    count += mergesort(right)

    i = j = k = 0
    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:  # No inversion if left is smaller than right
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]      
            k += 1
            j += 1

            # As left is sorted remaining elements in left-subarray (left[i+1], left[i+2] … left[mid]) will be greater than right[j].
            #These all elemnent including current element will cause inversion
            count += len(left) - i # position of larger element in left form behind
    
    while len(left) > i: # arr = 
        arr[k] = left[i] 
        i += 1 
        k += 1
    
    while len(right) > j:
        arr[k] = right[j]
        j += 1
        k += 1
    
    return count


arr = [1, 20, 6, 4, 5]  # 5
print(mergesort(arr))
print(arr)