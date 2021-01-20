'''
#### Name:  Write a program tofind the smallest window that contains all characters of string itself.
Link: [link]()

#### Sub_question_name: Sliding Window and HashMap 
Link: [link]()

1) Create a map of all the count of characters in the window
2) If distinct count matches required count of distinct characters then reduce or move window

'''

def smallest_window(s):
    distinct_chars = len(set(s))
    frequency = {}
    count = 0

    res_start = 0
    min_window_len = float('inf')

    start = 0  # Starting point of window
    for j, char in enumerate(s):
        if char in frequency.keys():
            frequency[char] += 1
        else:
            frequency[char] = 1
            count += 1

        if count == distinct_chars:
            # Got a solution
           
            while frequency[s[start]] > 1:   # if char at start is multiple copies, remove those
                frequency[s[start]] -= 1
                start += 1

            len_window = j - start + 1

            if len_window < min_window_len:
                min_window_len = len_window
                res_start = start

    print(s[res_start:res_start+min_window_len])

s = "aabcbcdbca"
# s = 'a'
smallest_window(s)    # dbca
