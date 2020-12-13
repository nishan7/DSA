'''
#### Name:  Common elements in all rows of a given matrix
Link: [link]()

Othe approach exists  
using hashing **O(r*c) O(c)**
'''


def common_elements(mat):
    old_set = set(mat[0])
    new_set = set()

    for row in mat[1:]:
        for element in row:
            if element in old_set:
                new_set.add(element)

        old_set = new_set
        new_set = set()

    print(old_set)


mat = [[1, 2, 3, 4, 5],     # 5
       [2, 4, 5, 8, 10],
       [3, 5, 7, 9, 11],
       [1, 3, 5, 7, 9], ]

common_elements(mat)
