'''
#### Name:  Naive Pattern Matching
Link: [link]()

'''

def string_match(string, pattern):
    n_s = len(string)
    n_p = len(pattern)

    for i in range(n_s - n_p +1):
        j = 0
        while( j< n_p):
            if string[i+j] != pattern[j]:
                break
            j += 1
        
        if j == n_p:
            return True
    
    return False


print(string_match('abaad','aa'))
