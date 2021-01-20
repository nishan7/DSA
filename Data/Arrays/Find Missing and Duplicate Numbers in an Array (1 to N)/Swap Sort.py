'''
#### Name:  Find Missing and Duplicate Numbers in an Array (1 to N)
Link: [link]()

#### Sub_question_name: Swap Sort 
Link: [link](https://www.youtube.com/watch?v=uo4kuV3pWfE&list=PL_z_8CaSLPWdJfdZHiNYYM46tYQUjbBJx&index=3)

### One missing and One duplicate
We read the input array and put into a swap to sorted array
as [2,3,1,5,1] to [1,2,3,1,5]

Then check array lineary with index value; if i+1 != arr[i] we found missing, duplicate


**TC: O(n)**
'''


def swap_sort(arr):
    n = len(arr)

    for i in range(n):
        if i+1 != arr[i]:
            current_value = arr[i]
            arr[i], arr[current_value-1] = arr[current_value-1], arr[i]


def find_missing_duplicates(arr):
    duplicate = -1
    missing = -1

    swap_sort(arr)

    for i in range(len(arr)):
        if i+1 != arr[i]:
            duplicate = arr[i]
            missing = i+1

    print(duplicate, missing)


arr = [2, 3, 1, 5, 1]
find_missing_duplicates(arr)
