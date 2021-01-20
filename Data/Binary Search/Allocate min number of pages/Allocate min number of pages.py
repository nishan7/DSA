'''
#### Name:  Allocate min number of pages
Link: [youtube](https://www.youtube.com/watch?v=2JSQIhPcHQg&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=21)
Link: [geeksforgeeks](https://www.geeksforgeeks.org/allocate-minimum-number-pages/)


Given number of pages in n different books and m students.
Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.

We apply binary search on maximum page that can be allocated to the student  
Ranging from minimum page to maximum page
'''
#  Check weather a pages can be allocated with certain mid(threshold maximum page to a single student)
def can_allocate(arr, stds, mid):
    std_count = 0
    idx = 0
    summer  = 0

    while idx < len(arr):
        summer += arr[idx]
        if summer == mid:
            summer = 0
            std_count += 1
        elif summer > mid:
            summer = 0
            std_count += 1
            idx += 1
        else:
            idx += 1
    
    if std_count == stds:
        return True
    else:
        return False


def find_min_pages(arr, stds):
    n = len(arr)
    # Pages that can be allocated to a student ranges from maximum page in arr (we try to minimize the page load for every student) and sum(arr).. as every student must get aleast one book
    low = max(arr)   # 0
    high = sum(arr)  # sum(arr)

    min_page = float('inf')

    while low <= high: 
        mid = (low + high)//2   # mid is maximum amount that a student can be allocated

        res = can_allocate(arr, stds, mid)
        if res == True:  # If is possible to allocate the page, we try to allocate using fewer pages
            min_page = min(min_page, mid)
            high = mid -1
        else:                # If is not posiible to allocate the page, we try using more pages
            low = mid + 1

    return min_page

arr = [10, 20, 30, 40]
arr = [12, 34, 67, 90]
std = 2
print(find_min_pages(arr, std))
