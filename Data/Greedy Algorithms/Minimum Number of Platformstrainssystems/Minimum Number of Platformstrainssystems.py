'''
#### Name:  Minimum Number of Platforms/trains/systems
Link: [link]()

**Brute** The idea is to take every interval one 
by one and find the number of intervals that overlap with it. 
Keep track of the maximum number of intervals that overlap with an interval. Finally, return the maximum value.

**Greedy**: Sort all event and count the platfrom required
1) If a train arrives to station (`platfrom_ctr += 1`)
1) If a train departs from station (`platfrom_ctr -= 1`)

**O(nlogn) O(1)**
'''


def min_plaform(arr, dept):
    arr.sort()
    dept.sort()
    n = len(dept)

    platform_ctr = 0
    max_platform_ctr = 0

    i = 0
    j = 0

    while i < n and j < n:
        if arr[i] < dept[j]:  # New train arrives at the platform
            platform_ctr += 1
            i += 1

        else:          # A train departs from the platform
            platform_ctr -= 1
            j += 1

        max_platform_ctr = max(max_platform_ctr, platform_ctr)

    # There are some train left in platform to depart, but who cares about them

    print(max_platform_ctr)


arr = [999,  940, 950,  1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

min_plaform(arr, dep)  # 3
