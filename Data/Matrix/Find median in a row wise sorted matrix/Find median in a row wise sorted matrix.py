'''
#### Name:  Find median in a row wise sorted matrix
Link: [gfg](https://www.geeksforgeeks.org/find-median-row-wise-sorted-matrix/)

## Check the link again
search a value such that (r*c + 1)//2 numbers  are less  than that value  

**O(rlog(c))**

'''

def bs(nums, key):
    
    low = 0
    high = len(nums) -1

    while low <= high:
        mid = (low + high)//2
        if key == nums[mid]:
            return mid + 1 # choose value right of 
        
        if key > nums[mid]:
            low = mid + 1
        
        else:
            high = mid -1 
    
    # after above while ends, low will higher index, value and high will have lower index value
    return low 

def binaryMedian(m, r, c):
    min_val = m[0][0]
    max_val = m[0][0]

    for i in range(r):
        min_val = min(min_val, m[0][0])
        max_val = max(max_val, m[0][c-1])

    desired = (r * c + 1)//2 # We assume r*c to be odd

    while min_val < max_val:  # Ends when min_val == max_val
        mid = (min_val + max_val)//2
        count = 0

        for j in range(r):
            places = bs(m[j], mid)  # Find where mid could be place, inturn it finds no. of elements samller than mid
            count += places
        
        if count < desired:    # Try to change min and max such that desired count can be reached
            min_val = mid + 1  # We can try to increase min_val to get greater count
        else:
            max_val = mid    # We can set the max_val to mid to set the max_val to constant  

    print(min_val)
    

r, c = 3, 3

m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]] 
binaryMedian(m, r, c) 

# print(bs(m[2],5 ))