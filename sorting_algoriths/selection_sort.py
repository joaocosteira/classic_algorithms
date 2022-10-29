#O(n2)

def findSmallest(arr): 
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest: 
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)     #find current smallest
        newArr.append(arr.pop(smallest)) #moves it to the new array
    
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([2, 2, 2, 1, 1]))
print(selectionSort([1]))
print(selectionSort([]))