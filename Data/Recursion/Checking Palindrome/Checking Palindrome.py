'''
#### Name:  Checking Palindrome
Link: [link]()

1) if single element then it is palindrome
2) if first and last element as per f and l doen't work out it is not palindrome
# NOT WORKING working for only even
'''


def check_palindrome(arr, f, l):
    if f == l:
        return True

    if arr[f] != arr[l]:
        return False

    if f <= l:
        return check_palindrome(arr, f+1, l-1)
    return False

print(check_palindrome('aabaa', 0, 4))
# Only even