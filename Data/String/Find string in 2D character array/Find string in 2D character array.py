'''
#### Name:  Find string in 2D character array
Link: [link]()

1) It might say character array or string or 2D matrix  
2) It can also say location,range,  count, present or not
'''


# def check(grid, i, j, key):
#     if -1 < i < m and -1 < j < n and grid[i][j] == key[0]:
#         return True

#     return False


def check(i, j):
    if -1 < i < m and -1 < j < n:
        return True

    return False


def search(grid, i, j, key, result, found_word):
    if key == '':
        if len(found_word) > 0:
            result.append(found_word.copy())
        return 

    if not check(i,j):
        return

    # if grid[i][j] == key[0]:
    #     found_word.append((i,j))
    # else:
    #     return 

    for _ in range(2):

        # if check(grid, i, j+1, key):
        found_word.append((i, j))
        search(grid, i, j+1, key[1:], result, found_word)
        found_word.pop()

        # if check(grid, i+1, j, key):
        found_word.append((i, j))
        search(grid, i+1, j, key[1:], result, found_word)
        found_word.pop()
        # found_word = search(grid, i+1, j+1, key, result, found_word)

    # return found_word


# grid = ["GEEKSFORGEEKS",
#         "GEEKSQUIZGEEK",
#         "IDEQAPRACTICE"]
grid = ['GEEKS']
m = len(grid)
n = len(grid[0])

key = "GEEKS"

result = []
found_word = []
search(grid, 0, 0, key,  result, found_word)
print(result)
