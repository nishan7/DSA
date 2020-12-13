'''
#### Name:  Sliding Window Maximum of Size k
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()

'''

def max_window(arr,k):
    n = len(arr)

    res = []
    for i in range(n-k+1):
        max_val = arr[i]
        for j in range(i, i+k):
            max_val = max(max_val, arr[j])
        res.append(max_val)

    print(res)


arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]   # [10, 10, 10, 15, 15, 90, 90]
k = 4
max_window(arr, k)