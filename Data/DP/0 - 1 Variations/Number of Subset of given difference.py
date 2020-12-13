'''
#### Name:  0 - 1 Variations
Link: [link]()

#### Sub_question_name: Number of Subset of given difference 
Link: [link](https://www.youtube.com/watch?v=ot_XBHyqpFc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=11)

```
s1 = (arr_sum + diff)/2
```

Find the subset count for s1 that is the solution

'''


def subset_sum_count(arr, n, req_sum):
    T = []
    for i in range(n+1):
        row = []
        for j in range(req_sum + 1):
            if j == 0:
                row.append(1)
            elif i == 0:
                row.append(0)
            else:
                row.append(-1)
        T.append(row)

    for i in range(1, n+1):
        for j in range(1, req_sum + 1):
            if arr[i-1] > j:
                T[i][j] = T[i-1][j]

            T[i][j] = T[i-1][j] + T[i-1][j - arr[i-1]]

    return T[n][req_sum]


def count_subset_diff(arr, n, diff):
    arr_sum = sum(arr)
    s1 = (arr_sum + diff)//2

    return subset_sum_count(arr, n, s1)


arr = [1, 1, 2, 3]
n = len(arr)
diff = 1

print(count_subset_diff(arr, n, diff))
