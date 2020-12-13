'''
#### Name:  Count Distinct Elements
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()

**O(n^2)**
'''


def count(arr):
    n = len(arr)
    res = 1 # First element is considered

    for i in range(1, n):
        repeated = False

        for j in range(0, i):
            if arr[i] == arr[j]:  # Item is repeated
                repeated = True
                break

        # if i == j+1:
        #     res += 1
        if not repeated:
            res += 1

    return res


arr = [4, 1, 2, 5, 2, 5]
print(count(arr))