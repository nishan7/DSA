'''
#### Name:  Quadruples of k sum
Link: [link]()

#### Sub_question_name: Hashing(N^2) 
Link: [link]()

'''

def quadruples(arr, req_sum):
    n = len(arr)

    sums = {}
    for i in range(n-1):
        for j in range(i+1, n):
            cur_sum = arr[i] + arr[j]
            if cur_sum in sums:
                sums[cur_sum].append((i,j))
            else:
                sums[cur_sum] = [(i,j)]
    
    # print(sums)

    # This will create a rane
    for i in range(n-1):
        for j in range(i+1,n):
            cur_sum = arr[i] + arr[j]
            target = req_sum  - cur_sum

            if target in sums.keys():
                for k,l in sums[target]:
                    if (i, j) != (k, l):
                        print(arr[i], arr[j], arr[k], arr[l])
                del sums[target]
            

A = [10, 2, 3, 4, 5, 9, 8]
k = 23
quadruples(A, k)
