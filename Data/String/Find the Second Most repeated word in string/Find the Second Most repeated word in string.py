'''
#### Name:  Find the Second Most repeated word in string.
Link: [link]()

'''


def second_freq(words):
    freq = {}

    first_max = 0
    second_max = 0

    for word in words:
        if word in freq.keys():
            freq[word] += 1
        else:
            freq[word] = 1

        if freq[word] > first_max:
            second_max = first_max
            first_max = freq[word]

    for word, f in freq.items():
        if f == second_max:
            print(word)
            break


words = ["ccc", "aaa", "ccc",
         "ddd", "aaa", "aaa"]

second_freq(words)
