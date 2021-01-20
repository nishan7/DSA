'''
#### Name:  Unbounded Knapsack Variations
Link: [link]()

#### Sub_question_name: Rod Cutting arr 
Link: [link]()

ditto from knapsack arr
'''

def rod_cutting(value, length):
    N = len(length)
    n =len(value)
    T = [0 for j in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, n+1):
            if length[j-1] <= i:
                T[i] = max(T[i], value[j-1]+T[i-length[j-1]])

    return T[-1]

value = [1, 5, 8, 9, 10, 17, 17, 20]
length = list(range(1, len(value)+1))  # Might be provided in the question

print(rod_cutting(value, length))