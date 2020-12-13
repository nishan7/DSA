'''
#### Name:  Sequence Pattern Matching
Link: [link]()

#### Sub_question_name: Linear 
Link: [link]()

'''


def is_present(X, key):
    m = len(X)
    n = len(key)

    i = 0
    j = 0

    while i < m:
        if X[i] == key[j]:
            j += 1
            i += 1
        else:
            i += 1
        
        if j == n:
            return True
    
    return False


X = 'AXYPCNY'
key = 'APN'

print(is_present(X, key))
