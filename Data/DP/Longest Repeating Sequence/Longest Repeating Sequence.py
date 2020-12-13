'''
#### Name:  Longest Repeating Sequence
Link: [link](https://www.youtube.com/watch?v=hbTaCmQGqLg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=30)

Almost same as lcs but matching character shouldn't have same index

'''

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    T = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1] and i-1 != j-1:   # No common index
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])  # abc fab; => bc fab || abc ab
    return T[m][n]


X = 'ABA'
X = 'ABA'
X = 'AABEBCDD'
print(lcs(X,X))