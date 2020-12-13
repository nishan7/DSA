'''
#### Name:  Pair with given sum in an unsorted array
Link: [link]()

#### Sub_question_name: BS for sorted 
Link: [link]()

'''

def get_pair_sums(arr, sum):
    low = 0
    high = len(arr)-1

    while low <= high:
        if arr[low] + arr[high] == sum:
            print(arr[low], arr[high])

        if arr[low] + arr[high] > sum:
            high = high - 1
        else:
            low = low + 1


arr = [1, 5, 7, 3, 3, -1, 5]
sum = 6
arr.sort()
get_pair_sums(arr, sum)
