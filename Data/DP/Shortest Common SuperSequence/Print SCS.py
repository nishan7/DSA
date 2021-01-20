'''
#### Name:  Shortest Common SuperSequence
Link: [link]()

#### Sub_question_name: Print SCS 
Link: [link](https://www.youtube.com/watch?v=VDhRg-ZJTuc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=29)

'''


def scs(X, Y):
    m = len(X)
    n = len(Y)

    T = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                # abc fab; => bc fab || abc ab
                T[i][j] = max(T[i-1][j], T[i][j-1])

    # Start from bottom right and move along
    i = m
    j = n
    output = ''

    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            output += X[i-1]
            i -= 1
            j -= 1

        elif T[i-1][j] > T[i][j-1]:  # When element in upper box is greater than left
            output += X[i-1]  # go upward, and use value from X or row string
            i = i-1       # We have decided to go upward, so we are ditching that row value and maximize lcs using upper value
        else:
            output += Y[j-1]  # Use the value from that column(Y), and go to left row
            j = j-1  # Ditched the current columns
        
    output = X[:i]+ Y[:j]+ output[::-1] 
    return output


X = 'AGGTAB'
Y = 'GXTXAYB'

print(scs(X, Y))
