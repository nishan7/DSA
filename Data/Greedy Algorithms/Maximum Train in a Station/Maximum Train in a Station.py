'''
#### Name:  Maximum Train in a Station
Link: [link]()

1) Similar to job sequencing and N meetings
2) Just keep train of departure time in slots

'''


def max_trains(data, platform):
    data.sort(key=lambda x: x[1])

    slot = [-1] * (platform + 1)  # Dept time of train on the platfrom
    train_ctr = 0
    for arr, dept, platform in data:
        if arr > slot[platform]:
            slot[platform] = dept
            train_ctr += 1

    print(train_ctr)


#  arr_time, dept_time, platfrom
data = [[1000, 1030, 1],
        [1010, 1020, 1],
        [1025, 1040, 1],
        [1130, 1145, 2],
        [1130, 1140, 2]]
platform = 2
max_trains(data, platform)   # 3
