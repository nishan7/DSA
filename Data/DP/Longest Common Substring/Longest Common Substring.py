'''
#### Name:  Longest Common Substring
Link: [link]()

'''


def lc_substring(X, Y):
    n = len(X)
    m = len(Y)

    T = [[0]*(m+1) for _ in range(n+1)]

    max_len = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
                max_len = max(max_len, T[i][j])
            # else:
            #     T[i][j] = 0  # this can be avoided as it is already zero

    return max_len

X = 'fabdexy'
Y = 'abdgxhpo'
print(lc_substring(X,Y))