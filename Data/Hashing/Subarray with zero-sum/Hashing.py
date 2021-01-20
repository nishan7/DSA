'''
#### Name:  Subarray with zero-sum
Link: [link]()

#### Sub_question_name: Hashing 
Link: [link]()

Iterate and find the current sum  and add to set()
If sum is 0 or sum is present in set() ; zero substring exists


**Prefix Sum**
arr[] = {1, 4, -2, -2, 5, -4, 3}

If we consider all prefix sums, we can
notice that there is a subarray with 0
sum when :
1) Either a prefix sum repeats or
2) Or prefix sum becomes 0.

Prefix sums for above array are:
1, 5, 3, 1, 6, 2, 5

Since prefix sum 1 repeats, we have a subarray
with 0 sum. 
'''

def check_zero(arr):
    n = len(arr)

    exist = set()
    running_sum = 0
    for num in arr:
        running_sum += num

        if running_sum == 0 or running_sum in exist:
            return True

        exist.add(running_sum)       

    return False


arr = [-3, 2, 3, 1,-1, 6]    
print(check_zero(arr))