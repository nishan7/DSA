'''
#### Name:  Merge 2 sorted Arrays
Link: [link]()

#### Sub_question_name: Similar to insertion sort 
Link: [link](https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/)

** [O(mn) time, O(1) space]**
'''

def sort_position(arr):
    # Insertion Sort
    n = len(arr)

    value = arr[0]
    j = 1
    
    while j<n and arr[j] < value:
        arr[j-1] = arr[j]  # Shift value to lower
        j += 1
    
    arr[j-1] = value # At position j we discovered element greater than `value` so we put value in j-1

def merge(a1, a2):
    m = len(a1)
    n = len(a2)

    # a1 will have smaller numbers and a2 will have larger numbers

    for i in range(m):
        if a2[0] < a1[i]:
            a2[0], a1[i] = a1[i], a2[0]
            
            sort_position(a2)  #Just put a2[0] in its right position



a1 = [1, 5, 9, 10, 15, 20]
a2 = [2, 3, 8, 13]
merge(a1, a2)   # Keep len(a1) >= a2
print(a1, a2)
