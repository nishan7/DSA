'''
#### Name:  Count of the frequency of array elements
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

**TC: O(n) SC: O(N)**
'''


def freq(arr):
    n = len(arr)

    f = {}

    for i in range(n):
        if arr[i] in f.keys():
            f[arr[i]] += 1
        else:
            f[arr[i]] = 1

    print(f)

arr = [4, 1, 2, 5, 2, 5]
freq(arr)
