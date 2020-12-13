'''
#### Name:  Sort a array
Link: [link](https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6)

'''


def sort(arr):

    if len(arr) == 1:
        return

    val = arr[-1]   # Get last value
    arr.pop()
    sort(arr)       # Sort Everything except last value
    insert(arr, val)  # Append the last value to sorted array


def insert(arr, val):
    # If possible just append the val to last of it
    if len(arr) == 0 or arr[-1] <= val:
        arr.append(val)
        return

    # if not e.g 2 in [1,5]; first get last_value(5); pop last_value till you can insert the val;
    last_val = arr[-1]
    arr.pop()
    insert(arr, val)
    arr.append(last_val)        # finally put back the last_val


arr = [3, 4, 0, 1]
print(arr)
