'''
#### Name:  Count Inversion
Link: [link]()

#### Sub_question_name: brute 
Link: [link]()

'''
def count_inv(arr):
    n = len(arr)

    ctr = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                ctr += 1
        
    print(ctr)

arr = [1, 20, 6, 4, 5] 
count_inv(arr)