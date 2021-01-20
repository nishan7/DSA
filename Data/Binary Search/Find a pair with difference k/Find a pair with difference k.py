'''
#### Name:  Find a pair with difference k
Link: [link]()
**Brute** 2 loops and compare **O(n)**
**BS** Sort and do BS; check and increment values of low and high as needed

'''


def find(arr, diff):
    n = len(arr)
    low = 0
    high = 1

    arr.sort()

    while low < n and high < n:
        # mid = (low + high)//2

        current_diff = abs(arr[low] - arr[high])
        if current_diff == diff:
            return arr[low], arr[high]

        elif current_diff > diff:
            low += 1
        elif current_diff < diff:
            high += 1

    return -1

arr = [1, 20, 8, 30, 40, 100]
n = 60
print(find(arr, n))
