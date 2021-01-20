'''
#### Name:  The celebrity Problem
Link: [link]()

#### Sub_question_name: Stacks 
Link: [link]()

1) Keep a maybe_celebrity stack and push every person
2) Pop 2 A and B person from the stack 
3) Remove one that isn't celebrity and keep one that can be celebrity

'''



def cel(matrix,n):
    maybe_celebrity = list(range(0, n//2))

    while len(maybe_celebrity> 0):
        

N = 8
  
# Person with 2 is celebrity  
MATRIX = [ [ 0, 0, 1, 0 ],  
           [ 0, 0, 1, 0 ],  
           [ 0, 0, 0, 0 ],  
           [ 0, 0, 1, 0 ] ] 


cel(MATRIX, N//2)