'''
#### Name:  Matrix Chain Multiplication
Link: [link]()

#### Sub_question_name: Memoization 
Link: [link](https://www.youtube.com/watch?v=9uUVFNOT3_Y&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=35)

'''

def mcm(arr, i, j, T):  # i,j are absolute index values
    if T[i][j] != -1:
        return T[i][j]

    if i == j:      # if return 0 if 0, 1, 2 elements; single matrix wont have multiplication
        return 0

    result  = float('inf') 
    for k in range(i, j): 
        c1 = mcm(arr, i, k, T) 
        c2 = mcm(arr, k+1, j, T)   
        c3 = arr[i-1] * arr[k] * arr[j]
        temp_ans = c1 + c2 + c3
        result = min(result, temp_ans)

    T[i][j] = result
    return result


arr = [40,20,30,10,30]   # [40*20, 20*30] + [30*10, 10*30] + [30 * 30 * 30]
# arr = [30,10,30]   # [40*20, 20*30] + [30*10, 10*30] + [30 * 30 * 30]
n = len(arr) 
T = [[-1]*(n+1) for _ in range(n+1)] # Create a table for i,j with size nxn; as maximum value of i or j can get is n

print(mcm(arr, 1, len(arr)-1, T))   # 26000
print()