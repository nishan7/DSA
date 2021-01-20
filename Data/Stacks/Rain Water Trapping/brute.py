'''
#### Name:  Rain Water Trapping
Link: [link]()

#### Sub_question_name: brute 
Link: [link]()


1) Input is array with has height of building 
2) What area covered with water, if it rains
3) Water above a build depends of largest building to its right and left

'''


def water_trapped(arr):
    

    output = []
    arr = [-1] + arr + [-1]
    n = len(arr)

    for i in range(1,n-1):
        mx_left = max(arr[:i])   # Max building to left
        mx_right = max(arr[i+1:])   # Max building to right

        if mx_left == -1 or mx_right == -1:  # Does not have building to hold water
            output.append(0)
        else:
            water_holding_height = min(mx_left, mx_right)  

            if water_holding_height > arr[i]:    # Check whether the current building is largest building
                water_above_it = water_holding_height - arr[i]
                output.append(water_above_it)
            else:
                output.append(0)

    return output

print(water_trapped([3,0,0,2,0,4]))
