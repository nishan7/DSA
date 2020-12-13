'''
#### Name:  Reversing
Link: [link]()

#### Sub_question_name: inplace 
Link: [link]()

Using 2 pointers

 '''

def reverse(arr):
     n = len(arr)

     for i in range(n//2):
         arr[i], arr[n-i-1]  = arr[n-i-1], arr[i]


arr = [1,2,4,6,7]
reverse(arr)
print(arr)