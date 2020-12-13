'''
#### Name:  Job Sequencing
Link: [link](https://www.geeksforgeeks.org/job-sequencing-problem/)

Link: [link](https://www.geeksforgeeks.org/job-sequencing-using-disjoint-set-union/)  # TODO

##### Brute Force
Get all subset and check all for feability

1) Sort all jobs in decreasing order of profit.
2) Initialize the result sequence as first job in sorted jobs.
3) Do following for remaining n-1 jobs
4) If the current job can fit in the current result sequence without missing the deadline, add current job to the result. Else ignore the current job.


**TC: O(n^2)**
'''


def job_sequencing(jobs, deadline, profit, t):
    n = len(jobs)
    index = list(range(n))
    # Sort the index based descending profit
    index.sort(key=lambda x: profit[x], reverse=True)

    slot = [-1] * (t+1)

    for i in index:
        job_name = jobs[i]
        deadline_time = deadline[i]

        for job_time in range(deadline_time, 0, -1):
            if slot[job_time] == -1:
                slot[job_time] = job_name
                break

    return slot


def job_sequencing(jobs, deadline, profit, t):
    n = len(jobs)
    index = list(range(n))
    data = [(p, d, job_name) for p, d, job_name in zip(profit, deadline, jobs)]
    data.sort(reverse=True)   # Sort by descending profit

    slot = [-1] * (t+1)

    for profit, deadline_time, job_name in data:

        for job_time in range(deadline_time, 0, -1):   # Try to put the higher profit first
            if slot[job_time] == -1:
                slot[job_time] = job_name
                break

    return slot


jobs = ['a', 'b', 'c', 'd', 'e']
deadline = [2, 1, 2, 1, 3]
profit = [100, 19, 27, 25, 15]
t = 3
print(job_sequencing(jobs, deadline, profit, t)[1:])
