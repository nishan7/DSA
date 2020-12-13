'''
#### Name:  Maximize array sum after K negations
Link: [link]()

#### Sub_question_name: Simple 
Link: [link]()


** O(NK)**
'''


def max_sum(arr, k):
    n = len(arr)

    for i in range(k):
        min_value = float('inf')
        min_idx = 0

        for idx, num in enumerate(arr):
            if num < min_value:
                min_value = num
                min_idx = idx

        if min_value > 0:
            return sum(arr)

        arr[min_idx] = -1 * arr[min_idx]
    return sum(arr)


arr = [-2, 0, 5, -1, 2]
k = 4 
print(max_sum(arr, k))     # 10
