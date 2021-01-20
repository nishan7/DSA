'''
#### Name:  Longest Common Substring
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

Palindromic Substring

'''

# Recursive use global variable

def lc_substring(X, Y, count):
    # print(X, Y, count)
    n = len(X)
    m = len(Y)

    # Base Conditon
    if n == 0 or m == 0:
        return count

    # Reduce Input

    if X[0] == Y[0]:
        count = lc_substring(X[1:], Y[1:], count+1)  # Find for smaller input
        # return count

    # Induction
    # Start count from 0
    count = max(count, lc_substring(X, Y[1:], 0), lc_substring(X[1:], Y, 0))

    return count


X = 'fabdexy'
Y = 'abdgxhpo'
count = 0
print(lc_substring(X, Y, count))


# Memoization
def lc_substring(X, Y, count, T):
    # print(X, Y, count)
    n = len(X)
    m = len(Y)

    # Base Conditon
    if n == 0 or m == 0:
        return count

    # Reduce Input

    if X[0] == Y[0]:
        count = lc_substring(X[1:], Y[1:], count+1,T)  # Find for smaller input
        # T[n][m] = count
        

    # Induction
    # Start count from 0
    count = max(count, lc_substring(X, Y[1:], 0,T), lc_substring(X[1:], Y, 0,T))

    T[n][m] = count
    return T[n][m]



X = 'fabdexy'
Y = 'abdgxhpo'

# Palindromic substring
X = 'chabbajx'
Y = X[::-1]

T = [[-1 for j in range(len(Y)+1)] for i in range(len(X)+1)]

print(lc_substring(X, Y, 0, T))   # 4

print()
