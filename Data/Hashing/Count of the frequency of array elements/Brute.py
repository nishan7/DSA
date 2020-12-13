'''
#### Name:  Count of the frequency of array elements
Link: [link](https://www.geeksforgeeks.org/counting-frequencies-of-array-elements/)

#### Sub_question_name: Brute 
Link: [link]()

**TC: O(n^2) SC: O(N)**
'''

def freq(arr):
    n = len(arr)
    visited = [False] * n # Visited array to track all the numbers


    for i in range(n):
        number = arr[i]

        if visited[number] == True:   # If already consider no need to check further
            continue

        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        
        visited[number] = True
        print(number, count)  # reducing 1 for its own count





arr = [4, 1, 2, 5, 2, 5]
freq(arr)