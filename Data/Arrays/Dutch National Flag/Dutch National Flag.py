'''
#### Name:  Dutch National Flag
Link: [link]()

'''

def dnf(arr):
    n = len(arr)
    low= 0
    high = n-1
    mid = 0

    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    print(arr)


arr = [0,1,0,1,2,0,1,2]  
dnf(arr)