'''
#### Name:  Mobile keypad
Link: [link]()

**O(n)**
'''


def convert(string):
    res = ''

    for char in string:
        if char == ' ':
            res += '0'
        else:
            position = ord(char) - ord('A')
            res += str[position]

    print(res)


str = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999"]

string = "GEEKSFORGEEKS"
convert(string)
