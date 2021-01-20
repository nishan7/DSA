'''
#### Name:  Array Pairs Sum
Link: [link]()

#### Sub_question_name: using hashtable 
Link: [link]()

** TC: O(2n) SC: O(n) **
 '''


def pairs(arr, k):
    ctr = dict()

    for num in arr:
        if num in ctr.keys():
            ctr[num] += 1
        else:
            ctr[num] = 1


    twice_count = 0
    for num in arr:
        target = k - num
        
        if target in ctr.keys():
            twice_count += ctr[target]

            if target == num: # if the number is same, remove it
                twice_count -= 1

    return twice_count//2


print(pairs([1,2,3,4,5,5],6))  # 3
            