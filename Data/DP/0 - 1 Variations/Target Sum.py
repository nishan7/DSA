'''
#### Name:  0 - 1 Variations
Link: [link]()

#### Sub_question_name: Target Sum 
Link: [link](https://www.youtube.com/watch?v=Hw6Ygp3JBYw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=12)


1) Assigning +/- to element of array to get a sum:
2) Same is subset of given difference
'''


def subset_sum(arr, req_sum, T):
    n = len(arr)
    if T[n][req_sum] != -1:
        return T[n][req_sum]

    if req_sum == 0:
        return 1
    if len(arr) == 0:
        return 0

    element = arr[-1]
    arr = arr[:-1]

    if element > req_sum:
        T[n][req_sum] = subset_sum(arr, req_sum, T)
        return T[n][req_sum]
    
    T[n][req_sum] = subset_sum(arr, req_sum, T) + subset_sum(arr, req_sum - element, T)
    return T[n][req_sum]


def target_sum_count(arr, target_sum):
    n = len(arr)
    arr_sum = sum(arr)
    s1 = (arr_sum + target_sum)//2  # target_sum is difference

    T = [[-1] * (s1+1) for i in range(len(arr)+1)]
    return subset_sum(arr, s1, T)


arr = [1, 1, 2, 3]
target_sum = 1

print(target_sum_count(arr, target_sum))

