'''
#### Name:  Count Sort
Link: [link]()

- Counting sort is a sorting technique based on keys between a specific range.
- Example: Range of 0 to 9 
 
**Time: O(n+k) Space: O(k) where n is size of input array and k is range of output**
'''


def count_sort(arr, n):
    output = [0] * n
    count = [0] * 10

    # Counting Frequency
    for i in range(n):
        count[arr[i]] += 1
    print(count)
    # count = [2, 0, 1, 2, 0, 0, 0, 0, 0, 1], here zero means the element doesn't exists

    # Getting Cumulative Frequency:
    for num in range(1, 10):
        count[num] = count[num] + count[num-1]
    print(count)
    # count = [2, 2, 3, 5, 5, 5, 5, 5, 5, 6]]

    for i in range(n):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return output


print(count_sort([9, 3, 3, 0, 0,2, 4, 7], 6))
