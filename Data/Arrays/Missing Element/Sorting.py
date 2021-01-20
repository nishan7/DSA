'''
#### Name:  Missing Element
Link: [link]()

#### Sub_question_name: Sorting 
Link: [link]()

- Sort both arrays
- Iterate using zip
- Index where element from both the array is not same is the missing element

 **TC: O(nlogn + nlogn + n) **
 '''

def find_missing(arr1, arr2):
     arr1.sort()
     arr2.sort()
     for a1, a2 in zip(arr1, arr2):
         if a1 != a2:
             return a1

print(find_missing([1,2,3,4,5], [4,5,6,2,1]))