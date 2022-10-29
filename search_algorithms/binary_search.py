def binary_search(list, item):
    
    low = 0
    high = len(list)  - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid 
        else:
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
    return  None

print(binary_search(list(range(0,1000,10)), 500))

#O(log2 n)


#Version with a flag, instead of a return inside the loop

def searchBinary(myList,item):

    low = 0
    high = len(myList) - 1
    found = False

    while( low < high and not found):
        mid = (low + high) / 2

        if myList[mid] == item:
            flag = True
        else:
            if item < myList[mid]:
                high = mid - 1
            else:
                low = mid + 1
    
    return mid if flag else None

print(binary_search(list(range(0,1000,10)), 500))
