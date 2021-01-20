'''
#### Name:  The celebrity Problem
Link: [link]()

#### Sub_question_name: Brute 
Link: [link]()

'''


def cel(matrix,n):
    celebrity = [1] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if matrix[i][j] == 0:
                celebrity[j] =0
            elif matrix[i][j] == 1:
                celebrity[i] = 0

    print(celebrity)

N = 8
  
# Person with 2 is celebrity  
MATRIX = [ [ 0, 0, 1, 0 ],  
           [ 0, 0, 1, 0 ],  
           [ 0, 0, 0, 0 ],  
           [ 0, 0, 1, 0 ] ] 


cel(MATRIX, N//2)