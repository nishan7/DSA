'''
#### Name:  Maximize array sum after K negations
Link: [link]()

#### Sub_question_name: Sorting 
Link: [link]()


**O(nlogn + n)**
'''


def max_sum(arr, k):
    n = len(arr)
    arr.sort()

    for idx, num in enumerate(arr):
        if num > 0:
            break

        arr[idx] = -1 * arr[idx]

    return sum(arr)


arr = [-2, 0, 5, -1, 2]
k = 4

print(max_sum(arr, k))     # 10
