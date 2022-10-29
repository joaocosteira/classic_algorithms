#Sum all elements of a list O(n)
def getSum(myList):
    sum = 0
    for item in myList:
        sum += item 
    return sum

# O(n2)
def getSumMatrix(myMatrix):
    sum = 0
    for row in myMatrix:
        for item in row:
            sum += item
    
    return sum

print(getSum([1,2,3,4,5]))
print(getSumMatrix([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]))