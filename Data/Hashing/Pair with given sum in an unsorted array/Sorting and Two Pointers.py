'''
#### Name:  Pair with given sum in an unsorted array
Link: [link]()

#### Sub_question_name: Sorting and Two Pointers 
Link: [link]()


# Cant work for mulitple solution 
**O(n + nlogn) O(n) for merge sort**

'''

def get_pair_sums(arr, sum):
    n = len(arr)
    i,j = 0, n-1

    while i < j:
        if arr[i] + arr[j] == sum:
            print(arr[i], arr[j])
            i -= 1

        elif arr[i] + arr[j] > sum:
            j -= 1
        else:
            i += 1


arr = [1, 5, 7, 3, 3, -1, 5]
sum = 6
arr.sort()
get_pair_sums(arr, sum)
