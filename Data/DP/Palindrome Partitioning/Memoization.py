'''
#### Name:  Palindrome Partitioning
Link: [link]()

#### Sub_question_name: Memoization 
Link: [link]()

'''
def isPalindrome(string):
    return string == string[::-1]

def part_pal(string, i, j, T):
    if T[i][j] != -1:
        return T[i][j]

    if i >= j:  # Single character or blank
        return 0
    
    if isPalindrome(string[i:j+1]):  # If any string after called is palindrome no need to partition
        return 0
    
    min_count = float('inf')
    for k in range(i, j):
        
        left = part_pal(string, i, k, T) 
        right = part_pal(string, k+1, j, T)    # Single Parition
        
        # Optimized memoization
        T[i][k] = left
        T[k+1][j] = right


        count = 1 + left + right
        min_count = min(min_count, count)
    
    T[i][j] = min_count
    return min_count

string = 'abaga'
n = len(string)
T = [[-1]*(n+1) for _ in range(n+1)]
print(part_pal(string, 0, len(string)-1, T))  

# abaga 2
print()