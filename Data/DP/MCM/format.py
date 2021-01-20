'''
#### Name:  MCM
Link: [link]()

#### Sub_question_name: format 
Link: [link]()


1) Range of i and j 
2) Base Condition
3) Range of k
4) Answer Function e.g min or max
'''

def solve(arr,i,j):

    if i<j:
        return arr

    for k in range(i,j):
        tmp_ans = solve(arr,i,k) + solve(arr, k+1, j)
        ans = function(temp_ans)
    
    return ans