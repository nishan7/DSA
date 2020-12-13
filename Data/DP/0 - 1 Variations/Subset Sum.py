'''
#### Name:  0 - 1 Variations
Link: [link]()

#### Sub_question_name: Subset Sum 
Link: [link](https://www.youtube.com/watch?v=_gPcYovP7wc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=7)

## Recursive Solution
Let isSubsetSum(arr, n, sum/2) be the function that returns true if 
there is a subset of arr[0..n-1] with sum equal to sum/2

The isSubsetSum problem can be divided into two subproblems
 a) isSubsetSum() without considering last element 
    (reducing n to n-1)
 b) isSubsetSum considering the last element 
    (reducing sum/2 by arr[n-1] and n to n-1)
If any of the above the above subproblems return true, then return true. 
isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
                              isSubsetSum (arr, n-1, sum/2 - arr[n-1])


if a subset exists that has sum k   
Weight and value is same single array of numbers


'''

from pprint import pprint


def has_subset(arr, req_sum, T):

    for i in range(1, len(arr)+1):
        for j in range(1, req_sum+1):
            if arr[i-1] > j:  # if a element is greater than the req_sum
                T[i][j] = T[i-1][j]

            elif arr[i-1] <= j:
                T[i][j] = T[i-1][j] or T[i-1][j-arr[i-1]]

    return T[len(arr)][req_sum]


arr = [2, 3, 7, 8, 10]
n = len(arr)
req_sum = 11

T = []
for i in range(n+1):
    row = []
    for j in range(req_sum+1):
        if j == 0:
            row.append(True)
        elif i == 0:
            row.append(False)
        else:
            row.append(False)
    T.append(row)

print(has_subset(arr, req_sum, T))
# pprint(T)


