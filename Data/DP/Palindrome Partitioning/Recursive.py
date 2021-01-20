'''
#### Name:  Palindrome Partitioning
Link: [link](https://www.youtube.com/watch?v=szKVpQtBHh8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=36)

#### Sub_question_name: Recursive 
Link: [youtube](https://www.youtube.com/watch?v=szKVpQtBHh8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=36)


'''

def isPalindrome(string):
    return string == string[::-1]

def part_pal(string, i, j):
    if i >= j:  # Single character or blank
        return 0
    
    if isPalindrome(string[i:j+1]):
        return 0
    
    min_count = float('inf')
    for k in range(i, j):
        count = 1 + part_pal(string, i, k) + part_pal(string, k+1, j)

        min_count = min(min_count, count)
    
    return min_count

string = 'abaga'
print(part_pal(string, 0, len(string)-1))