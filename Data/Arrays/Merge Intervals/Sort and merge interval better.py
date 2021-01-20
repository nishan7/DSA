'''
#### Name:  Merge Intervals
Link: [link]()

#### Sub_question_name: Sort and merge interval better 
Link: [link]()

'''


def merge_interval(intervals):
    intervals.sort()

    temp = intervals[0]
    res = []

    for interval in intervals:
        if interval[0] <= temp[1]:  # (a,b) (c,d) b<=c ; Then merge
            temp[1] = max(interval[1], temp[1])
        else:                      # Push as it is
            res.append(temp)
            temp = interval

    res.append(temp)  # There may remain a last one that is not appended
    print(res)


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]   # [[1, 6], [8, 10], [15, 18]]
# intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]   # [[1,9]]
merge_interval(intervals)
