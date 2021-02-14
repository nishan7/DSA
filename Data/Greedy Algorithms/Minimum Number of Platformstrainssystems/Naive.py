'''
#### Name:  Minimum Number of Platforms/trains/systems
Link: [link]()

#### Sub_question_name: Naive 
Link: [link]()

'''


def min_plaform(arr, dept):
    n = len(arr)

    max_platfrom = -1
    for i in range(n):
        ctr = 1

        for j in range(i+1, n):

            # j train ko aaunu rw jaane ko beech ma i aauxa ki vice versa
            if arr[j] <= arr[i] <= dept[j] or arr[i] <= arr[j] <= dept[i]:   
                ctr += 1

        max_platfrom = max(max_platfrom, ctr)

    print(max_platfrom)


arr = [999,  940, 950,  1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

min_plaform(arr, dep)  # 3
