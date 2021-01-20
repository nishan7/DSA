'''
#### Name:  Program to generate all possible valid IP addresses from given  string.
Link: [link]()


**O(N^3) O(n) Space for temp string**
'''

def check(ip):
    parts = ip.split('.')

    for i in parts:
        if len(i) > 3:  # Len Less than 3 wont occur
            return False

        if int(i) > 255:
            return False
        
        if len(i) > 1 and i[0] == '0': # Any number can have prefix 0
            return False
        
    return True
    
    

def valid_ip(s):
    n = len(s)
    result = []

    # Just do a check for size of ip
    if n > 12 and n < 4:
        return False

    for i in range(1, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                ip = s[:i] + '.' + s[i:]            # 2.5525511135
                ip = ip[:j+1] + '.' + ip[j+1:]      # 2.5.525511135  # We increment by 1 as . is placed
                ip = ip[:k+2] + '.' + ip[k+2:]      # 2.5.525511135

                # print(ip)       2.5.5.25511135
                if check(ip):
                    result.append(ip)
    
    print(result)

s = "25525511135"
valid_ip(s)    # ['255.255.11.135', '255.255.111.35']