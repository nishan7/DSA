'''
#### Name:  Merge Intervals
Link: [link]()

#### Sub_question_name: Sort and Check All 
Link: [link]()

! wrong
'''


# def merge_intervals(arr):
#     n = len(arr)
#     arr.sort(key=lambda x: x[0])
#     res = []

#     for i in range(n-1):
#         for j in range(i+1, n):
#             range1 = arr[i]
#             range2 = arr[j]

#             if range2[0] <= range1[1]:  # (2, 4) (3, 7)
#                 new_range = [range1[0], max(range1[1], range2[1])]   # (2, 7)
#                 # res.append(new_range)
#                 arr[i] = new_range

#         res.append(arr[i])

#     print(res)


# arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# merge_intervals(arr)
