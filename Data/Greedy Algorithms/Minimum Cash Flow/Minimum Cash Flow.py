'''
#### Name:  Minimum Cash Flow
Link: [link]()


1) Create net about for every person
2) Find max value and index for every debit and credit
3) Choose minimum and maximum value 
'''


def get_max(arr):
    max_value, max_idx = 0, 0

    for idx, value in enumerate(arr):
        if max_value < value:
            max_value = value
            max_idx = idx

    return max_value, max_idx


def min_cash(graph):
    n = len(graph)
    amount = [0] * n
    credit = [0] * n
    debit = [0]*n

    for i in range(n):
        for j in range(n):
            amount[i] -= graph[i][j]
            amount[j] += graph[i][j]

    for idx, value in enumerate(amount):
        if value >= 0:
            debit[idx] = value
        else:
            credit[idx] = -value

    while True:
        debit_value, debit_idx = get_max(debit)
        credit_value, credit_idx = get_max(credit)
        if debit_value == 0:
            break

        if debit_value < credit_value:
            debit[debit_idx] = 0
            credit[credit_idx] = credit_value - debit_value
            print("{} Paid  {} to {}".format(debit_idx, debit_value, credit_idx))
        
        else:
            credit[credit_idx] =0
            debit[debit_idx] = debit_value - credit_value
            print("{} Paid  {} to {}".format(credit_idx, credit_value, debit_idx))


graph = [[0, 1000, 2000],
         [0, 0, 5000],
         [0, 0, 0]]

min_cash(graph)
