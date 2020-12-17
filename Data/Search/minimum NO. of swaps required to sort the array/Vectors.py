'''
#### Name:  Minimum no. of swaps required to sort the array
Link: [link]()

#### Sub_question_name: Vectors 
Link: [link]()

Using pair<item, index> and do something similar to swap sort
'''

def swaps(nums):
    n = len(nums)
    vector = [(nums[i], i) for i in range(n)]
    vector.sort()

    ans = 0
    i = 0
    while i < n:
        if i == vector[i][1]:
            i += 1
            continue
        else:
            ans += 1
            actual_loc = vector[i][1]
            vector[i],vector[actual_loc] = vector[actual_loc], vector[i] 
    
        if vector[i] != i: # Swap until it is sorted
            i -= 1
        else:
            i += 1


    print(ans)

a = [101, 758, 315, 730,
     472, 619, 460, 479]
swaps(a)
