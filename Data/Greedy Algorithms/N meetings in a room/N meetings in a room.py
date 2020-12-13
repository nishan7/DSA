'''
#### Name:  N meetings in a room
Link: [link]()

Activity Selection Problem
1) Sort the meeting my finish_time
2) Keep track of finish_time in variable next_meeting_time
3) Iterate to find other meeting that is possible
'''

def meetings(n,s,f):
    index = list(range(n))
    index.sort(key=lambda i: f[i])

    res = []
    next_meeting_time = 0

    for meeting_no in index:
        if s[meeting_no] > next_meeting_time:  # if this meeting can be done
            res.append(meeting_no)
            next_meeting_time = f[meeting_no]
    
    print([idx+1 for idx in res])






s = [ 1, 3, 0, 5, 8, 5 ]
f = [ 2, 4, 6, 7, 9, 9 ]
n = len(s)

meetings(n,s,f)