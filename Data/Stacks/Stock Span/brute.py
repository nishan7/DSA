'''
#### Name:  Stock Span
Link: [link]()

#### Sub_question_name: brute 
Link: [link]()



'''
def stock(arr):
    n = len(arr)
    output = [1]

    for i in range(1,n):
        ctr = 1
        key = arr[i]
        for j in range (i-1, -1, -1):
            if arr[j] <= key:
                ctr += 1
        output.append(ctr)

    return output

print(stock([1,2,4,5,3]))