'''
#### Name:  Insertion Sort
Link: [link](https://www.geeksforgeeks.org/insertion-sort/)

To sort an array of size n in ascending order:
1) Iterate from arr[1] to arr[n] over the array.
2) Compare the current element (key) to its predecessor.
3) If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

**O(n^2) inplace stable**
'''


def insertion_sort(arr, n):

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key #Consider a condition of j == -1, then set j+1(0) to save the value  


arr = [4, 5, 11, 3, 0, 6]
insertion_sort(arr, len(arr))
print(arr)
