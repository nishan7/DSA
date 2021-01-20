'''
#### Name:  Converting Roman Numerals to Decimal
Link: [link]()

We can also use dictionary for 2 chars too
'''

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def convert(number):
    prev = 0
    ans = 0

    for i in range(len(number)-1, -1, -1):
        char = number[i]

        value_of_char = roman[char]

        if value_of_char > prev:   # XL, for L
            ans += value_of_char
        else:                  # XL, for X
            ans -= value_of_char

        prev = value_of_char       # Store this value for next iteration

    print(ans)


convert('MCXI')   # 1111
convert('MCXLI')  # 1141
convert('MCMIV')  # 1904
