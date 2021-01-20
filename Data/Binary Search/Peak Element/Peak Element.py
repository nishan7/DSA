'''
#### Name:  Peak Element
Link: [youtube](https://www.youtube.com/watch?v=OINnBJTRrMU&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=17)  


Link: [leetcode](https://leetcode.com/problems/find-peak-element/) 



**Brute Force**: Linear O(n) with keeping track of prev element and comparing; return when criteria match

BS on answer; as we need only single answer from all the answers
Peak element is a element is greater than its neighbours  (There may be mulitple peak elements, print either of them)
1) Also check for last and first element too
'''


def findPeakElement(nums) -> int:
    arr = nums
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2

        if mid > 0 and mid < n-1:   # Making sure it is not first or last element

            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:   # Others
                return mid
            elif arr[mid+1] > arr[mid]:
                low = mid+1
            elif arr[mid-1] > arr[mid]:
                high = mid-1

        elif n == 1:             # If only single element exists
            return mid

        elif mid == 0:   # If mid reaches first element
            if arr[mid] > arr[mid+1]:   
                return mid
            else:
                return mid+1

        elif mid == n-1:  # If the mid reaches last element
            if arr[mid] > arr[mid-1]:   
                return mid
            else:
                return mid-1


# nums = [1, 4, 3, 2, 8, 11, 9, 9]
nums = [2, 5, 1, 7, 11, 15, 14]
print(nums[findPeakElement(nums)])
