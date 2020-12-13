'''
#### Name:  Shortest Common SuperSequence
Link: [youtube](https://www.youtube.com/watch?v=VDhRg-ZJTuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29)

We have to find a shortest string that contains both the original string in the correct sequence   
We use LCS to the the common sequeuence and `len(s1+s2)-lcs` is the shortest superseqeuence   


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


def scs(X, Y):
    total_len = len(X+Y)
    lcs_value = lcs(X, Y)
    return total_len - lcs_value       # Total length minus Common Sequence Lenght is the answer


X = 'AGGTAB'
Y = 'GXTXAYB'

print(scs(X, Y))
