'''
#### Name:  Subarray with given sum
Link: [link]()

#### Sub_question_name: Count of subarrays 
Link: [link]()

## Only for zero 

1) Iterate throught the array a calcuate sum
2) Sum at point j is 0 , output j
3) Else put the sum in hashset
4) If sum already presentt in hashset, it means a[i]... a[j] == 0
'''


def count_subarray(arr, req_sum):
    n = len(arr)

    sums = dict()
    current_sum = 0

    out = []

    for i in range(n):
        current_sum += arr[i]

        if current_sum == 0:
            out.append((0, i))

        if current_sum in sums.keys():
            out += [(start+1, i) for start in sums[current_sum]]
            sums[current_sum].append(i)

        else:
            # Store index as a list; as many such indices may exists
            sums[current_sum] = [i]

    print(out)


# arr = [2, 3, 5, 1]
# req_sum = 6

arr = [6, 3, -1, -3, 4, -2,  2, 4, 6, -12, -7]
req_sum = 0   # [(2, 4), (2, 6), (5, 6), (6, 9), (0, 10)]


n = len(arr)
count_subarray(arr, req_sum)
# req_sum = 0
