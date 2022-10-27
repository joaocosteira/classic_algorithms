def linear_search(list,item):
    
    for i in range(len(list)):
        if list[i] == item:
            return i

    return None

print(linear_search(list(range(10,100,10)),90))

#O(n)