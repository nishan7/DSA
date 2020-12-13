'''
#### Name:  Longest Palindromic Subsequence
Link: [link](https://www.youtube.com/watch?v=wuOOOATz_IA&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=26)

LCS between string and reverse string will give size of palindromic string
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
                # T[i][j] = 0
    return T[m][n]



X = 'agbcba'
print(lcs(X, X[::-1]))