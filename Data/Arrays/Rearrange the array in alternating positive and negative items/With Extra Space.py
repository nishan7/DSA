'''
#### Name:  Rearrange the array in alternating positive and negative items
Link: [link]()

#### Sub_question_name: With Extra Space 
Link: [gfg](https://www.geeksforgeeks.org/move-ve-elements-end-order-extra-space-allowed/)

1) Use a temp array to copy +ve and negative numbers into arrays

**O(n) O(n)**

'''


def rearrange(arr):
    n = len(arr)
    pos_temp = []
    neg_temp = []

    for num in arr:
        if num < 0:
            neg_temp.append(num)

    for num in arr:
        if num >= 0:
            pos_temp.append(num)

    i, j = 0, 0
    m = len(pos_temp)
    n = len(neg_temp)

    k = 0
    while i < m and j < n:
        if m > n:
            arr[k] = pos_temp[i]
            arr[k+1] = neg_temp[j]
        else:
            arr[k] = neg_temp[i]
            arr[k+1] = pos_temp[j]

        k += 2
        i += 1
        j += 1

    # Put the last element
    arr[k] = pos_temp[i] if i < m else neg_temp[j]

    print(arr)


arr = [1, -1, -3, -2, 7, -5, 6]
rearrange(arr)
