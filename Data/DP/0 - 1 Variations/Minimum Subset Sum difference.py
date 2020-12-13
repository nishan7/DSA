'''
#### Name:  0 - 1 Variations
Link: [link]()

#### Sub_question_name: Minimum Subset Sum difference 
Link: [link](https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10)


Find the range of parition
'''

from pprint import pprint

def get_subset(arr, n):
    arr_sum = sum(arr)

    T = []
    for i in range(n+1):
        row = []
        for j in range(arr_sum+1):
            if j == 0:
                row.append(True)
            elif i == 0:
                row.append(False)
            else:
                row.append(False)
        T.append(row)

    for i in range(1, n+1):
        for j in range(1, arr_sum+1):
            if arr[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-arr[i-1]]


    return T[n] #  Get the whole possibly of subsets when all the items are considered

def minimum_diff(arr, n):
    arr_sum = sum(arr)
    subsets_possible = get_subset(arr, n)
    parition1 = subsets_possible[:arr_sum//2+1]  # Only considering values form 0 to mid +1 to ensure positive values afterwards
    parition1_values = [idx for idx, value in enumerate(parition1) if value]
    min_value = float('inf')
    
    for elem in parition1_values:
        min_value = min(min_value, arr_sum - 2*elem)   # partiton2 - parition1; (arr_sum-parition1)-parition1; arr_sum - "*parition1"
    return min_value



arr = [1,2,7]  #4
n = len(arr)


print(minimum_diff(arr, n))