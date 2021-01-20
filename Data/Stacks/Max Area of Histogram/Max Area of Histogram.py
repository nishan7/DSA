'''
#### Name:  Max Area of Histogram
Link: [link]()

Array of height of building, denoting histogram

Form a largest rectangle and return its area

Find NSL and NSR and Form a Rectangle between that

**O(n) Since Every bar is pushed and popped only once**
'''


def nsl(arr):
    n = len(arr)

    stack = [(arr[0], 0)]
    output = [-1]

    for i in range(1, n):

        while stack:
            if stack[-1][0] < arr[i]:
                output.append(stack[-1][1])
                stack.append((arr[i], i))
                break
            else:
                stack.pop()

        if len(stack) == 0:
            output.append(-1)
            stack.append((arr[i], i))

    return output


def nsr(arr):
    n = len(arr)
    output_rev = [n]  # We use n as the righmost index index of -1
    stack = [(arr[-1], n-1)]

    for i in range(n-2, -1, -1):

        while stack:
            if stack[-1][0] < arr[i]:
                output_rev.append(stack[-1][1])
                stack.append((arr[i], i))
                break
            else:
                stack.pop()

        if len(stack) == 0:
            output_rev.append(n)
            stack.append((arr[i], i))

    return output_rev[::-1]


def histo(arr):
    n = len(arr)

    left = nsl(arr)
    right = nsr(arr)

    width = [r-l-1 for l, r in zip(left, right)]  # We donot include the nsr and nsl values in this

    area = [w * h for w, h in zip(width, arr)]    # arr[i] being the height

    mx = max(area)
    idx = area.index(mx)
    
    return arr[idx], mx


arr = [6, 2, 5, 4, 5, 1, 6]

print(histo(arr))


#  [6, 2, 5, 4, 5, 1, 6]  left =>[-1, -1, 1, 1, 3, -1, 5] right => [1, 5, 3, 5, 5, 7, 7]
#  width = [1, 5, 1, 3, 1, 7, 1]   area = [6, 10, 5, 12, 5, 7, 6]
#  4, 12
