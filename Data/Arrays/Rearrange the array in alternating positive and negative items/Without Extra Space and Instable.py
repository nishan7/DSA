'''
#### Name:  Rearrange the array in alternating positive and negative items
Link: [link]()

#### Sub_question_name: Without Extra Space and Instable 
Link: [gfg](https://www.geeksforgeeks.org/rearrange-array-in-alternating-positive-negative-items-with-o1-extra-space-set-2/?ref=rp)

1) Replace the items, (can also use quicksort)
2) Move positive to back and negative to front
3) Then alternate them
# Not working
**O(n) O(1)  Instable**
'''


def rearrange(arr):
    n = len(arr)

    i = 0
    j = n-1

    while i < j:
        if arr[i] < 0:
            i += 1
        elif arr[j] >= 0:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    print(arr)
    # arr[i] is positive value
    k =0 
    while k < n and i<n:
        arr[k], arr[i] = arr[i], arr[k]
        k += 2
        i += 1

    print(arr)

arr = [1, -1, -3, -2, 7, -5, 6]
rearrange(arr)
