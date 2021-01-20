'''
#### Name:  Find Missing and Duplicate Numbers in an Array (1 to N)
Link: [link]()

#### Sub_question_name: Multiple Swap Sort 
Link: [link](https://www.youtube.com/watch?v=G4_OxJGonQY&list=PL_z_8CaSLPWdJfdZHiNYYM46tYQUjbBJx&index=4)

Multiple Missing elements

New have to check the swapping index for multiple duplicates

Doesn't work for constant array

**TC: O(n) **

'''

def swap_sort(arr):
    n = len(arr)
 
    for i in range(n):      # may use i < len(arr)
        if arr[i] != i+1:
            # if arr[i] == arr[arr[i]-1]:  # It may a condition where element we are trying to swap is in correct place
            #     continue

            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]

def find_missing(arr):
    swap_sort(arr)
    print(arr)
    missing = []
    duplicates = []

    for i in range(len(arr)):
        if i+1 != arr[i]:
            duplicates.append(arr[i])
            missing.append(i+1)
    
    print(duplicates, missing)


arr = [2,3,1,8,2,3,5,1]
find_missing(arr)
# print(arr)