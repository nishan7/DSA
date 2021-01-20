'''
#### Name:  Quick Sort
Link: [link]()
1) Choose last element as pivot
2) Run from low to high
    - If any element larger than pivot, swap wiht arr[i]
    - increment i+=1
3) Swap arr[i+1] with pivot element
4) All the elements on the left side of the pivot elements are smaller and right side are larger

**O(n^2) || O(nlogn) || SC: O(nlogn) || not stable || inplace ||**
'''


def partition(arr, low, high):
    pivot = arr[high]  # selecting last index as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # if any element larger than pivot then swap wiht arr[i]
   # i+1 index denote next smallest element to place next
    arr[i+1], arr[high] = arr[high], arr[i+1]   # swap arr[i+1] wiht pivot
    # All the element in left side of pivot are smaller and right side of pivot are larger
    print(arr, arr[i+1])

    return i+1  # index of parition


def qs(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        qs(arr, low, p-1)
        qs(arr, p+1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

qs(arr, 0, n-1)
print(arr)
