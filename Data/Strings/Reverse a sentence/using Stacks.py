'''
#### Name:  Reverse a sentence
Link: [link]()

#### Sub_question_name: using Stacks 
Link: [link]()

'''

# Quick way to reverse
def reverse_quick(s):
    # or return ' '.join(reversed(s.split()))
    return ' '.join(s.split()[::-1])



# Reversed sentneces using stacks
def rev_sentence_stacks(s):
    words = []   # Stack
    length = len(s)

    i = 0
    while i < length:

        if s[i] != ' ':   # if a character is not space
            word_start = i

            while i < length and s[i] != ' ':  # Get a word
                i += 1

            words.append(s[word_start:i])  # append to the word

        i += 1

    return ' '.join(reversed(words))  # return the stack in reversed order


print(rev_sentence_stacks("A quick brown fox jumps over a wall"))
print(reverse_quick("A quick brown fox jumps over a wall"))
