'''
#### Name:  Array Pairs Sum
Link: [link]()

#### Sub_question_name: using set 
Link: [link]()

- ***Can be used with repeating elements*** 


**TC: O(n) SC: O(n)**

 '''
 
def pairs_sum(arr, k):
    seen = set()

    for num in arr:
        target = k -num
        if target in seen:
            print(num, target)
        else:
            seen.add(num)

pairs_sum([1,2,3,4,5,5],6)
