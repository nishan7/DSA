'''
#### Name:  Maximum sum such that no 2 elements are adjacent
Link: [link]()

'''

def find_max(nums):
    n = len(nums)

    incl = nums[0]      # Sum including previous element
    excl = 0            # Sum excluding previous element

    for number in nums[1:]:
        new_excl = max(excl, incl)  # We are excluding this number
        
        incl = excl + number   # We add number in excl and previous element was excluded from `excl`
    
        excl = new_excl
    
    print(max(incl, excl))

arr = [5, 5, 10, 100, 10, 5] 
find_max(arr)