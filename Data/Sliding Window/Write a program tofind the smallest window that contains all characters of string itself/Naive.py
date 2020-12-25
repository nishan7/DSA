'''
#### Name:  Write a program tofind the smallest window that contains all characters of string itself.
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()


Just use some sets and do this
in **O(N^2) O(N)**
'''

def smallest_window(s):
    if len(s) == 1:
        print(1)
        return

    alphabets = set(s)
    ans = float('inf')
    for i in range(len(s)-1):
        for j in range(i, len(s)):
            window = s[i:j+1]
            if alphabets == set(window):
                ans = min(ans, len(window))
    print(ans)

# s = "aabcbcdbca"
s = 'a'
smallest_window(s)