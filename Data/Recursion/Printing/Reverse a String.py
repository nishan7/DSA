'''
#### Name:  Printing
Link: [link]()

#### Sub_question_name: Reverse a String 
Link: [link]()

'''
def reverse(s, idx):
    if idx == 0:
        return s[idx]

    return s[idx] + reverse(s, idx-1)


print(reverse('string', 6-1))
