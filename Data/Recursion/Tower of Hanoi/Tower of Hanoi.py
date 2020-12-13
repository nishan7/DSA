'''
#### Name:  Tower of Hanoi
Link: [link](https://www.youtube.com/watch?v=l45md3RYX7c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=11)

If odd(1) => from src to dest
elif even => from src to temp



'''
count = 0
def hoi(n, src, temp, dest):
    global count
    count += 1
    # Base Condition
    if n== 1:
        print("Move {} from {} to {}".format(n, temp, dest))
        return 

    
    # Hypothesis in smaller input
    hoi(n-1, src, dest, temp)
    print("Move {} from {} to {}".format(n, temp, dest))
    hoi(n-1, temp, src, dest)
    

hoi(3, 'S','T','D')
print(count)