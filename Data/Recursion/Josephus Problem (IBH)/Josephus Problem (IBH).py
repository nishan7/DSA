'''
#### Name:  Josephus Problem (IBH)
Link: [link](https://www.youtube.com/watch?v=ULUNeD0N9yI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=19)

n = 40 men are circle and every 7th person is killed; Then find which one is remaining


'''

'''
Recursive Way
'''

def josephus(arr, n, starting_person):

    if n == 1:  # Last person to remain is the answer
        return arr[0]

    person_to_kill = (starting_person + k) % n   # Find the person to kill next
    arr.pop(person_to_kill)
    starting_person = person_to_kill
    return josephus(arr, n-1, starting_person)


n = 40
k = 7
k = k-1  # As we are counting from the person himself

arr = [i for i in range(1, n+1)]
print(josephus(arr, n,  0))  # Start from index 0

# n =40, k=7 => 24;   n=5, k=2 => 3


'''
Iterative Way
'''

n = 5
k = 2
k = k-1  # As we are counting from the person himself

arr = [i for i in range(1, n+1)]
starting_person = 0
while len(arr) > 1:
    n = len(arr)
    person_to_kill = (starting_person + k) % n
    arr.pop(person_to_kill)
    starting_person = person_to_kill

print(arr[0])
