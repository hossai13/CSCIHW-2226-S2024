def negativeIntegers(x):
    count = 0
    
    for i in x:
        if i < 0:
            count += 1
    return count

def largestEvenIntegers(x):
    largestEven = 0
    location = 0
    
    for i in range(len(x)):
        if x[i] % 2 == 0 and x[i] > largestEven:
            largestEven = x[i]
            location = i
            
    return largestEven, location

def smallestInteger(x):
    smallestInt = x[0]
    
    for i in x:
        if i < smallestInt:
            smallestInt = i
            
    return smallestInt

list = [-14, 2, 5, 4, -4, -2, 1, 12]
print("There are", negativeIntegers(list), "negative integers in the list.")
print("The largest even integer is", largestEvenIntegers(list)[0], "at index", largestEvenIntegers(list)[1])
list = [12, 33, 4, 6, 9, 11, 3]
print("The smallest integer is", smallestInteger(list))
