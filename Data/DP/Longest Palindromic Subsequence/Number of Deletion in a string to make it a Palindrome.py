'''
#### Name:  Longest Palindromic Subsequence
Link: [link]()

#### Sub_question_name: Number of Deletion in a string to make it a Palindrome 
Link: [link](https://www.youtube.com/watch?v=CFwCCNbRuLY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=28)


Find LCS, and len(X) - LCS
'''

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    T = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])  # abc fab; => bc fab || abc ab
    return T[m][n]

X = "agxbcbna"
lcs_value = lcs(X, X[::-1])

print(len(X)-lcs_value)