'''
#### Name:  Pair with given sum in an unsorted array
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

'''
def getPairsCount(arr, n, sum):
    m = {}
    twice_count=0
    for number in arr:
        if number not in m.keys():
            m[number] = 1
        else:
            m[number] += 1

    for i in range(0, n):
        another_num = sum-arr[i]
        if another_num in m.keys():
            twice_count += m[another_num]

        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    return twice_count //2


arr = [1, 5, 7, 3, 3, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is", getPairsCount(arr,n, sum))