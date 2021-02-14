'''
#### Name:  Median of 2 sorted arrays of equal size
Link: [link]()

'''


def median(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    m1 = -1
    m2 = -1

    median = (m + n)//2

    i, j, k = 0, 0, 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            m2 = m1
            m1 = nums1[i]

            k += 1
            i += 1

        else:
            m2 = m1
            m1 = nums2[i]

            k += 1
            j += 1

        if k == median:
            break

    if (m+n) % 2 == 1:   # If odd
        print(m1)
    else:                # If even
        print((m1+m2)//2)


nums1 = [1, 12, 15, 26, 38]
nums2 = [2, 13, 17, 30, 45]

# nums1 = [2, 3, 5, 8]
# nums2 = [10, 12, 14, 16, 18, 20]
median(nums1, nums2)
