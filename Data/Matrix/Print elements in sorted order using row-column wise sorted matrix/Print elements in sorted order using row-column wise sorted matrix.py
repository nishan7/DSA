'''
#### Name:  Print elements in sorted order using row-column wise sorted matrix
Link: [link]()

Use merges sort wala merging


**O(r*c) O(n)** 
'''


def merge(a, b):
    temp = []

    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            temp.append(a[i])
            i += 1

        else:
            temp.append(b[j])
            j += 1


    temp += a[i:]
    temp += b[j:]

    return temp


def sort_mat(mat):
    res = []
    for row in mat:
        res = merge(res, row)
    
    print(res)


mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

print(sort_mat(mat))


