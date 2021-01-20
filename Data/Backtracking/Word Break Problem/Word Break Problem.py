'''
#### Name:  Word Break Problem
Link: [link]()



'''


def ww(vector, inp, d):
    if inp == '':
        print(vector)

    for word in d:
        if inp.startswith(word):
            vector.append(word)
            ww(vector, inp[len(word):], d)
            vector.pop()   # Bracktract


d = ["mobile", "samsung", "sam", "sung",
     "man", "mango", "icecream", "and",
     "go", "i", "love", "ice", "cream"]

vector = []
inp = 'ilovesamsungmobile'
ww(vector, inp, d)
inp = 'iloveicecreamandmango'
ww(vector, inp, d)
