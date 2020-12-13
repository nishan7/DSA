'''
#### Name:  Minimum Cost to cut a board into squares
Link: [gfg](https://www.geeksforgeeks.org/minimum-cost-cut-board-squares/)

1) Cut expensive edges first, as they will incur heavier penalities due to no_of_cuts.


'''


def min_cuts( X, Y):
    m = len(X)
    n = len(Y)

    X.sort(reverse=True)
    Y.sort(reverse=True)

    i = 0
    j = 0
    no_of_hor_cuts = 1
    no_of_ver_cuts = 1
    cost = 0

    while i < m and j < n:
        if X[i] > Y[j]:   # Vertical cuts, |
            cost += X[i] * no_of_hor_cuts

            no_of_ver_cuts += 1
            i += 1
        else:              # Horizontal cuts   ---
            cost += Y[j] * no_of_ver_cuts

            no_of_hor_cuts += 1
            j += 1

    # Collect the rest
    total = sum(X[i:])
    cost += total * no_of_hor_cuts

    total = sum(Y[j:])
    cost += total * no_of_ver_cuts

    # print(cost)
    return cost


X = [2, 1, 3, 1, 4]
Y = [4, 1, 2]
X = [2]
Y = [1]
min_cuts( X, Y)
