'''
#### Name:  Minimum # of deletion and insertion to convert String A to String B
Link: [link](https://www.youtube.com/watch?v=VDhRg-ZJTuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29)

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


def minimum(X, Y):
    lcs_value = lcs(X,Y)
    return len(X) - lcs_value, len(Y)-lcs_value


X = 'AGGTAB'
Y = 'GXTXAYB'

print(minimum(X, Y))
