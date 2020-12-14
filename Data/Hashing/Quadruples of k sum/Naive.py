'''
#### Name:  Quadruples of k sum
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()

**O(n^4)**
'''


def quadruples(arr, req_sum):
    n = len(arr)
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    # print(arr[i], arr[j], arr[k], arr[l])
                    if arr[i] + arr[j] + arr[k] + arr[l] == req_sum:
                        print(arr[i], arr[j], arr[k], arr[l])


A = [10, 2, 3, 4, 5, 9, 7, 8] 
k = 23
quadruples(A, k)
