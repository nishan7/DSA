'''
#### Name:  Square root of a Number
Link: [link]()

#### Sub_question_name: BS 
Link: [link]()

'''

# Floor square root


def sqrt(number):
    i = 1
    low = 1
    high = number

    while low <= high:
        mid = (low + high)//2

        if mid * mid == number:
            return mid

        elif number > mid*mid:
            low = mid + 1
            ans = mid    # Set the answer to the lower end of range

        elif number < mid*mid:
            high = mid - 1

    return ans

print(sqrt(4))
print(sqrt(11))
print(sqrt(49))
