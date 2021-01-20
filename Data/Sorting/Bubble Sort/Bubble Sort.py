'''
#### Name:  Bubble Sort
Link: [link](http:\\geeks for geeks.com)


It compare every element of array with its adjacent element.

**O(n^2) Stable in-place**
'''

def bubble(arr,n):
    for i in range(n): # First to last
        for j in range(0, n-1-i): # First to Last - i
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

arr = [3,14,5,12,9]
bubble(arr, len(arr))
print(arr)