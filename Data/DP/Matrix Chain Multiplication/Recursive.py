'''
#### Name:  Matrix Chain Multiplication
Link: [link](https://www.youtube.com/watch?v=D7AFvtnDeMU&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=33)

#### Sub_question_name: Recursive 
Link: [link](https://www.youtube.com/watch?v=kMK148J9qEE&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=34)

Matrix Multiplication is not commutative
 Given a sequence of matrices(dimension e.g 10x20), find the most efficient way to multiply these matrices together. 
 The problem is not actually to  perform the multiplications, but merely to decide in which order to perform the multiplications. 
'''

def mcm(arr, i, j):  # i,j are absolute index values
    if i == j:      # if return 0 if 0, 1, 2 elements; single matrix wont have multiplication
        return 0

    result  = float('inf') 
    for k in range(i, j): 
        c1 = mcm(arr, i, k) 
        c2 = mcm(arr, k+1, j)   
        c3 = arr[i-1] * arr[k] * arr[j]
        temp_ans = c1 + c2 + c3
        result = min(result, temp_ans)

    return result


# arr = [40,20,30,10,30]   # [40*20, 20*30] + [30*10, 10*30] + [30 * 30 * 30]
arr = [30,10,30]   # [40*20, 20*30] + [30*10, 10*30] + [30 * 30 * 30]
print(mcm(arr, 1, len(arr)-1))   # 26000