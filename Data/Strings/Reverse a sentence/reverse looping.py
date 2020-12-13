'''
#### Name:  Reverse a sentence
Link: [link]()

#### Sub_question_name: reverse looping 
Link: [link]()

'''

def revv(s):
    n = len(s)
    ctr = n-1
    temp = ""
    while ctr >= 0:
        end=ctr
        start=ctr
        
        #Detect a space
        while(s[ctr] != " " and ctr >= 0):
            print(s[ctr]) 
            ctr -= 1
        start = ctr+1
        
        # Add the to temp string
        for idx in range(start, end+1):
            temp += s[idx]
        
        if ctr >=0:
            temp += ' '  # Not to add space for last one

        # print(ctr)

        ctr -= 1 # Decrease the ctr to go to next char

    return temp

revv('Hello John how are you')
