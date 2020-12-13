'''
#### Name:  Count Distinct Elements
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

**TC: O(n) SC: O(n)**

'''

def count(arr):
    n = len(arr)
    res = 0

    numbers = set()

    for i in range(n):
        if arr[i] in numbers:
            continue
        else:
            numbers.add(arr[i])
            res += 1

    return res


arr = [4, 1, 2, 5, 2, 5]
print(count(arr))