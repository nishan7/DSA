'''
#### Name:  LRU
Link: [link]()

'''


def lru(process_list, capacity):
    pf = 0
    memory = []
    for p in process_list:
        if p not in memory:
            if len(memory) == capacity:
                memory.pop(0)
                memory.append(p)
            else:
                memory.append(p)

            pf += 1
        else:         # Refresh the page
            memory.remove(p)
            memory.append(p)

    print(pf)


capacity = 4
processList = [7, 0, 1, 2, 0, 3, 0,
               4, 2, 3, 0, 3, 2]

lru(processList, capacity)     # 6
