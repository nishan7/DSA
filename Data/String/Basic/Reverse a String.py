'''
#### Name:  Basic
Link: [link]()

#### Sub_question_name: Reverse a String 
Link: [link]()

'''

s= ["a", "b","c"]

n = len(s)
for i in range(n//2):
    s[i] , s[n-1-i] = s[n-1-i], s[i]

print(s)