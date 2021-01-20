'''
#### Name:  Floor/Ceil of an Element in sorted array
Link: [link]()

#### Sub_question_name: Next alphabet in sorted Array 
Link: [link](https://www.youtube.com/watch?v=X45c37QMdX0&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=12)

Similar to ceil, we just need ceil of key; next alphabet is returned even if key exists

'''


def next_elem(arr, key):
    low = 0
    high = len(arr) - 1
    res = ''

    while low <= high:
        mid = (low+high)//2

        if key == arr[mid]:
            low = mid+1

        elif key < arr[mid]:
            high = mid-1
            res = arr[mid]
        elif key > arr[mid]:
            low = mid+1

    # return res
    return arr[low]  #my way


arr = ['a', 'c', 'e','e', 'g', 'j']
key = 'c'
print(next_elem(arr, key))
