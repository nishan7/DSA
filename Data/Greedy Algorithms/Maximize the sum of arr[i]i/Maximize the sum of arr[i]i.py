'''
#### Name:  Maximize the sum of arr[i]*i
Link: [link]()

'''


def max_prod(arr):
    arr.sort()

    res = 0
    for idx, num in enumerate(arr):
        res += idx * num

    print(res)


arr = [3, 5, 6, 1]
max_prod(arr)   # 31