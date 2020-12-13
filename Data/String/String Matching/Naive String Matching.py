'''
#### Name:  String Matching
Link: [link]()

#### Sub_question_name: Naive String Matching 
Link: [link]()

'''


def string_matching(s, pattern):
    m = len(s)
    n = len(pattern)

    for i in range(m-n+1):

        for j in range(n):
            if pattern[j] != s[i+j]:
                break

        else:   # If it doesn't fail
            return True

    return False


s = 'todaygoodday'
pattern = 'goodx'
print(string_matching(s, pattern))
