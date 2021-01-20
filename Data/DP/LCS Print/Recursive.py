'''
#### Name:  LCS Print
Link: [link]()

#### Sub_question_name: Recursive 
Link: [link]()

'''
# Recursive answer
def lcs(x, y):
    n = len(x)
    m = len(y)

    if n == 0 or m == 0:
        return ''

    if x[0] == y[0]:
        # One matching element, check for others
        return x[0] + lcs(x[1:], y[1:])

    lcs1 = lcs(x, y[1:])
    lcs2 = lcs(x[1:], y)

    if len(lcs1) > len(lcs2):
        return lcs1
    else:
        return lcs2


x = "AGGTAB"
y = "GXTXAYB"

print(lcs(x, y))

# Memoization Answer

def lcs(x, y, T):
    n = len(x)
    m = len(y)

    if T[n][m] != -1:
        return T[n][m]

    if n == 0 or m == 0:
        return ''

    if x[0] == y[0]:
        # One matching element, check for others
        T[n][m] = x[0] + lcs(x[1:], y[1:], T)
        return T[n][m]

    lcs1 = lcs(x, y[1:], T)
    lcs2 = lcs(x[1:], y, T)

    if len(lcs1) > len(lcs2):
        T[n][m] = lcs1
        return T[n][m]
    else:
        T[n][m]= lcs2
        return T[n][m]


x = "AGGTAB"
y = "GXTXAYB"
T = [[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]

print(lcs(x, y, T))
print()
