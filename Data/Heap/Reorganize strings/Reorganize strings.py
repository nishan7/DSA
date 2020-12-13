'''
#### Name:  Reorganize strings
Link: [link]()

'''
from heapq import heappush, heappop
heap = []


def h_push(x): return heappush(heap, (-1*x[1], x[0] ))


def h_pop():
    freq, alpha= heappop(heap)
    return alpha, -1 * freq


def reorganize(S):
    counter = {}
    for s in S:
        if s in counter.keys():
            counter[s] += 1
        else:
            counter[s] = 1

    freq_values = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    if 2*freq_values[0][1] - 1 > len(S):
        return ''

    # print(freq_values)
    for alpha, freq in freq_values:
        h_push((alpha, freq))

    res = []
    while len(heap) > 0:
        alpha, freq = h_pop()
        # We can place most freq values in first index or alternative
        if len(res) == 0 or alpha != res[-1]:
            res.append(alpha)

            if freq > 1:
                h_push((alpha, freq - 1))

        else:                                 # For not freq
            alpha1, freq1 = h_pop()  # Get new pair out
            res.append(alpha1)

            h_push((alpha, freq))  # Push old ones

            if freq1 > 1:
                h_push((alpha1, freq1-1))

    print(''.join(res))


S = "aaab"
reorganize(S)
