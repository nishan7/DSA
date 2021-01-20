'''
#### Name:  Missing Element
Link: [link]()

#### Sub_question_name: hashtable 
Link: [link]()

- Create a frequency table for arr2
- Iterate through arr1 and subtract count in dict of arr2
- The element with value 0 in dict of arr2 is missing value
 '''


def find_missing(arr1, arr2):
    darr1 = dict()

    for element in arr2:
        if element in darr1.keys():
            darr1[element] += 1
        else:
            darr1[element] = 1
    
    for element in arr1:
        if element not in darr1.keys() or darr1[element]==0:
            return element
        else:
            darr1[element] -= 1
    
    return -1

print(find_missing([1,2,3,4,5], [4,5,6,2,1]))
