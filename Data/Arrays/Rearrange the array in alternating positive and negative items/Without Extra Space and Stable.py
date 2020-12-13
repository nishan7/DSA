'''
#### Name:  Rearrange the array in alternating positive and negative items
Link: [link]()

#### Sub_question_name: Without Extra Space and Stable 
Link: [gfg](https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/)

**O(n) O(1) stable**
'''


def rearrange(arr):
    n = len(arr)

    i = -1

    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    neg, pos = 0, i+1
    print(arr)

    # Make order into alternate
    if (n-pos) > (pos-neg):          # [1, -3, 7, -1, 5, -2, 6] if no of positive numbers are more
        pass
    else:                    # [-1, 7, -2, 1, -3, 6, -5] if no_of_negatives numbers are more
        neg = 1

    while pos < n and neg < pos and arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2

    print(arr)


arr = [1, -1, -3, -2, 7, 5, 6]   # [1, -3, 7, -1, 5, -2, 6]
arr = [1, -1, -3, -2, -7, 5, 6]   # [-1, 1, -2, 5, -3, 6, -7]
rearrange(arr)
