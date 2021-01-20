'''
#### Name:  Quadruples of k sum
Link: [link]()

#### Sub_question_name: N^3 
Link: [link]()

It is two pointer search in a range
Doesn't work for multiple answers (After getting a answer there is no optimal way to increment it)

**O(nlogn n^3)**

'''


def quadruples(arr, req_sum):
    n = len(arr)
    arr.sort()

    # This will create a rane
    for i in range(n-3):
        for j in range(i+1, n-2):
            l = i + 1
            r = j-1

            while l < r:
                cur_sum = arr[i] + arr[j] + arr[l] + arr[r]
                if cur_sum == req_sum:
                    print(arr[i], arr[j], arr[l], arr[r])
                    
                if cur_sum > req_sum:
                    r -= 1
                else:
                    l += 1

A = [10, 2, 3, 4, 5, 9, 7, 8]
k = 23
quadruples(A, k)
