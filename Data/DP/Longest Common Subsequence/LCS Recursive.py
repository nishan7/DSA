'''
#### Name:  Longest Common Subsequence
Link: [link]()

#### Sub_question_name: LCS Recursive 
Link: [link](https://www.youtube.com/watch?v=4Urd0a0BNng&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=19)

**O(2^n)**
Base Condition

'''


def lcs(x, y):
    n = len(x)
    m = len(y)

    if n == 0 or m == 0:
        return 0

    if x[-1] == y[-1]:
        # One matching element, check for others
        return 1 + lcs(x[:-1], y[:-1])

    return max(lcs(x, y[:-1]), lcs(x[:-1], y))


x = "AGGTAB"
y = "GXTXAYB"

print(lcs(x, y))
