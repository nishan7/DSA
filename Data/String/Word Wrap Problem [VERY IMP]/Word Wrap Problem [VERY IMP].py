'''
#### Name:  Word Wrap Problem [VERY IMP]
Link: [link]()

!! NOT optimal
'''


def word_wrap(words, capacity):
    n = len(words)
    line = 0
    i = 0

    while i < n:
        line_space = -1
        line_start = i

        while  i < n and line_space + words[i] + 1 <= capacity:
            line_space = words[i] + 1
            line_end = i
            i += 1

        print(line_start+1, line_end+1, end=" ")


words = [3, 2, 2, 5]
capacity = 6

word_wrap(words, capacity)
