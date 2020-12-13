'''
#### Name:  Check if one string is a rotation of another
Link: [link]()

1) 2 Input string s1 and s2
2) Create a temp as s1 + s1 and check if it contains s2 as substring
'''


def is_present(s1, s2):
    temp = s1 + s1

    if len(s1) != len(s2):
        return 0

    if temp.count(s2) > 0:
        return 1
    else:
        return 0


A = 'ABCD'
B = 'CDAB'

print(is_present(A, B))
