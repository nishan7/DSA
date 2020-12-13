'''
#### Name:  Max and Min N candies
Link: [link]()
In a candy store there are N different types of candies available and the prices of all the 
N different types of candies are provided. There is also an attractive offer by candy store. 
We can buy a single candy from the store and get at-most K other candies (all are different types) for free.

1) Find minimum amount of money we have to spend to buy all the N different candies.
2) Find maximum amount of money we have to spend to buy all the N different candies.

**TC: (nlogn + n + n)**
'''

def minmax(candies, k):
    n = len(candies)
    candies.sort()

    # Min
    i = 0
    j = n
    min_cost = 0
    while i<j:
        min_cost += candies[i]  # Add first(cheaper) candies to weight 
        i += 1
        j -= k     # Add last(expensive) candies and k-offer

    # Max
    i = n-1
    j = -1
    max_cost = 0

    while i > j:
        max_cost += candies[i]
        i -= 1
        j += k

    print(min_cost, max_cost)






n = 4
k = 2
candies = [3, 2, 1, 4]
minmax(candies, k)