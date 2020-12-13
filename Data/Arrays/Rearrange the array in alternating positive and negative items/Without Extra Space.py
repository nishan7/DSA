'''
#### Name:  Rearrange the array in alternating positive and negative items
Link: [link]()

#### Sub_question_name: Without Extra Space 
Link: [link]()

'''
def rearrange(arr):
    n = len(arr)
    temp = []

    for num in arr:
        if num < 0:
            temp.append(num)

    for num in arr:
        if num >= 0:
            temp.append(num)

    print(temp)


arr = [1, -1, -3, -2, 7, 5, 11, 6]
rearrange(arr)
