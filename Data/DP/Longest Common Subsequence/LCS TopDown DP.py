'''
#### Name:  Longest Common Subsequence
Link: [link]()

#### Sub_question_name: LCS TopDown DP 
Link: [link](https://www.youtube.com/watch?v=hR3s9rGlMTU&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=21)



'''


def lcs(x, y):

    # As base conditon is 0; as starting number for maximum is also 0
    T = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]

    # We go from top row, column by column to last row
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i-1] == y[j-1]:  # We found one more common item
                T[i][j] = 1 + T[i-1][j-1]

            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])

    return T[len(x)][len(y)]


x = "AGGTAB"
y = "GXTXAYB"


print(lcs(x, y))

print()
