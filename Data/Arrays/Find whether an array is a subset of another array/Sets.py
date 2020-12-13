'''
#### Name:  Find whether an array is a subset of another array
Link: [link]()

#### Sub_question_name: Sets 
Link: [link]()

'''


def is_subset(nums1, nums2):
    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1

    superset = set(nums1)
    for number in nums2:
        if number not in superset:
            return False

    return True


nums1 = [11, 1, 13, 21, 3, 7]
nums2 = [11, 3, 7, 1]
print(is_subset(nums1, nums2))
