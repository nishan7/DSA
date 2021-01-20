'''
#### Name:  K-th element of two sorted Arrays
Link: [link]()

#### Sub_question_name: Modified Merge Sort's merge 
Link: [link]()

Similar to one in merge sort but just dont need to use temp array
**O(n) O(1)**
'''


def merged_loc(nums1, nums2, req_index):
    i, j, k = 0, 0, -1

    while i < len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:
            k += 1
            if k == req_index:
                print(nums1[i])
                return
            i += 1
        else:
            k += 1
            if k == req_index:
                print(nums2[j])
                return
            j += 1

    while k != req_index and i < len(nums1):
        k += 1
        if k == req_index:
            print(nums1[i])
            return
        i += 1

    while k != req_index and j < len(nums2):
        k += 1
        if k == req_index:
            print(nums2[j])
            return
        j += 1

    # if k != req_index and  i < len(nums1):
    #     cur_val = nums1[i + (req_index - k-1)]

    # if k != req_index and j < len(nums2):
    #     cur_val = nums2[j + (req_index - k-1)]


nums1 = [2, 3, 6, 7, 9]
nums2 = [1, 4, 8]

merged_loc(nums1, nums2, 7)
merged_loc(nums1, nums2, 0)
