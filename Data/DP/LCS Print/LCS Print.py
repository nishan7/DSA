'''
#### Name:  LCS Print
Link: [link]()

'''


def lcs_substring(X, Y):
    n = len(X)
    m = len(Y)

    T = [['']*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = X[i-1] + T[i-1][j-1]
            else:
                # For X=abc and Y = eab; Try to match X=abc with Y=ab; and other one
                # T[i][j] = max(T[i-1][j], T[i][j-1]) 
                if len(T[i-1][j]) > len(T[i][j-1]):
                    T[i][j] = T[i-1][j]
                else:
                    T[i][j] = T[i][j-1]

    return T[n][m][::-1]


x = "AGGTAB"
y = "GXTXAYB"

print(lcs_substring(x, y))
print()

# Aditya verma way
def lcs_substring(X, Y):
    n = len(X)
    m = len(Y)

    T = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])   # For X=abc and Y = eab; Try to match X=abc with Y=ab; and other one


    output = ''
    i = n
    j = m
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            output += X[i-1]
            i = i-1
            j = j-1
        else:
            if T[i][j-1] > T[i-1][j]:  # Greater one is the place where the string is matched
                j = j-1
            else:
                i =i-1
    
    return output[::-1]




x = "AGGTAB"
y = "GXTXAYB"

print(lcs_substring(x, y))
