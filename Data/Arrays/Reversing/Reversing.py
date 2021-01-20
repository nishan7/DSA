'''
# Name:  Reversing
Link: [link]()

'''


def reverse(arr):
    n = len(arr)

    res = []
    for i in range(n-1, -1, -1):
         res.append(arr[i])
    
    return res


arr = [1,2,4,6,7]
print(reverse(arr))

