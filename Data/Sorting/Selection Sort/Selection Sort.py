'''
#### Name:  Selection Sort
Link: [link]()

**O(n^2) Not Stable, in-place**

change

'''


def selection_sort(arr, n):
    for i in range(n):
        min = i
        for j in range(i, n): # or range(i+1, n)
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]


arr = [34, 12, 8, 4]
selection_sort(arr, len(arr))
print(arr)
