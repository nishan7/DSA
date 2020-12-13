'''
#### Name:  First negative number in every window of size k
Link: [link](https://www.youtube.com/watch?v=uUXXEgK2Jh8&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=4)

Brute is loop dual loop of i and j   
Fixed window

Keep track of negative number in a list

'''


def negative_numbers(arr, k):
    n = len(arr)
    i = 0 # left most of window
    j = 1 # Right most of window

    neg_numbers = []

    while j < n:
        if arr[j] < 0:  # j is exclusive
            neg_numbers.append(arr[j])

        if j-i+1 < k:  # fixed window size
            j += 1
        elif j-i+1 == k:
            if arr[i] < 0:  # if a negative number is no longer going to be in window,pop it out
                if len(neg_numbers) > 0:
                    print(neg_numbers[0])
                    # Remove the number from neg_number as it is out of window
                    neg_numbers.pop(0)
                else:
                    print(0)

            else:
                if len(neg_numbers) > 0:
                    print(neg_numbers[0])
                else:
                    print(0)

            i += 1
            j += 1


arr = [12, -1, -7, -8, 30, 16, 28, -15]     # -1 -1 -7 -8 0 -15
k = 3
negative_numbers(arr, k)

