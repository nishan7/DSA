'''
#### Name:  Longest Common Prefix
Link: [leetcode](https://leetcode.com/problems/longest-common-prefix/solution/)

#### Sub_question_name: Brute 
Link: [link]()

**O(mn) O(1) m is size of list, n is size of maximum string**
'''



def lcp(strs):
    if len(strs) == 0:
        return ''

    first = strs[0]
    for idx in range(len(first)):
        
        for string in strs:
            if idx < len(string) and string[idx] == first[idx] :
                continue
            else:
                return first[:idx]
    
    return first


print(lcp(["a"]))
print(lcp(["flower","flow","flight"]))
