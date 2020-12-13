'''
#### Name:  Rain Water Trapping
Link: [youtube_link Aditya Verma](https://www.youtube.com/watch?v=FbGG2qpNp4U&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=9)


1) Input is array with has height of building 
2) What area covered with water, if it rains
3) Water above a build depends of largest building to its right and left

'''


def water_trapped(arr):
    output = []
    n = len(arr)

    mxl = [0]*n    # We will be filling all the values, so initalizing value is irrelavent
    mxr = [0]*n

    # Finding maximum element in left subarray, account for current element
    init = arr[0]
    for i in range(n):
        # Switching these 2 line will make it consider or not consider the current element
        init = max(arr[i], init)
        mxl[i] = init

    # Finding maximum in right subarray for every element
    init = arr[-1]
    for i in range(n-1, -1, -1):
        init = max(arr[i], init)
        mxr[i] = init

    # print(mxl, mxr)
    surrounding_height = [min(l, r) for l, r in zip(mxl, mxr)]

    water_over_it = [sh - h for sh, h in zip(surrounding_height, arr)]
    print(water_over_it)

    return sum(water_over_it)

print(water_trapped([3, 0, 0, 2, 0, 4]))


#  [3, 0, 0, 2, 0, 4] => [0, 3, 3, 1, 3, 0]   water capacity is 10 units