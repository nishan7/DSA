'''
#### Name:  Missing Element
Link: [link]()

#### Sub_question_name: xor 
Link: [link]()

- perform the xor of all the elements 

**NOT WORKING*
'''

def find_missing(arr1, arr2):
    result = 0
    for number in arr1+arr2:
        result  ^= number
        print(result)
    
    return result

print(find_missing([1,2,3,4,5], [4,5,6,2,1]))

