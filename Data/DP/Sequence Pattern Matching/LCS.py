'''
#### Name:  Sequence Pattern Matching
Link: [link](https://www.youtube.com/watch?v=QVntmksK2es&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=31)

#### Sub_question_name: LCS 
Link: [link](https://www.youtube.com/watch?v=QVntmksK2es&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=31)

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



X = 'AXYPCNY'
key = 'APNZ'

if lcs(X,key) == len(key):
    print("True")
else:
    print("False")