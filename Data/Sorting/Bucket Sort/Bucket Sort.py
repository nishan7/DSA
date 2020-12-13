'''
#### Name:  Bucket Sort
Link: [link]()

Bucket Sort is a sorting technique that sorts the elements by first dividing the elements into several groups called buckets. And we sort those buckets

**TC:  O(N+K)  SC: O(N) stable if underlying sort is stable , not inplace**
'''


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = i
        j = i-1

        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def bucket_sort(arr, n):
    buckets = [[] for _ in range(10)]  # for integers

    for i in range(n):
        idx = int(arr[i]*10)
        buckets[idx].append(arr[i])

    for idx in range(len(buckets)):
        buckets[idx] = insertion_sort(buckets[idx])

    for idx in range(len(buckets)):
        for bucket_idx in range(len(buckets[idx])):
            arr[k] = buckets[idx][bucket_idx]
            k += 1


arr = [0.3, .45, .89, .21, .11, .56]
bucket_sort(arr, 6)
print(arr)
