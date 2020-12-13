'''
#### Name:  Longest Common Subsequence
Link: [link]()

#### Sub_question_name: LCS Memoization 
Link: [link]()

'''

def lcs(x, y, T):
    n = len(x)
    m = len(y)

    if T[n][m] != -1:
        return T[n][m]

    if n == 0 or m == 0:
        return 0

    if x[-1] == y[-1]:
        # One matching element, check for others
        T[n][m]= 1 + lcs(x[:-1], y[:-1], T)
        return T[n][m]


    T[n][m] =  max(lcs(x, y[:-1], T), lcs(x[:-1], y, T))
    return T[n][m]


x = "AGGTAB"
y = "GXTXAYB"

T = [[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]

print(lcs(x, y, T))   # 4

print()