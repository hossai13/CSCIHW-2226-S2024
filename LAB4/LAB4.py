import math

# Position Search: Finding the index of the maximum number in the array. 
def max(array):
    max = array[0]
    for i in range(1, len(a)):
        if max < array[i]:
            max = array[i]
    return max

# Linear Search: Finding a target element x in a sequece of integers.
def linearSearch(array, x):
    print()
    i = 0
    while i < len(array) and array[i] != x:
        print("i = ", i, " |  a[i] = ", array[i])
        i += 1
    if i < len(array):
        location = i
        return location
    else:
        return -1

# Binary Search: Finding a target element x in an increasing ordered sequence of integers.
def binarySearch(array, x):
    i = 0
    j = len(array) - 1
    print()
    while i < j:
        m = math.floor((i + j) / 2)
        print ("i = ", i, " |  j = ", j, " |  m = ", m, " |  a[i] = ", array[i], " |  a[m] = ", array[m])
        if x > array[m]:
            i = m + 1
        else:
            j = m
    if x == array[i]:
        location = i
    else:
        location = -1
    return location


# Bubble Sort: Finding a target element x in an increasing ordered sequence of integers.
def bubbleSort(array):
    print()
    n = len(array)
    for i in range(n):
        for j in range(n-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                print ("i = ", i, " |  j = ", j, " |  a[j] = ", array[j], " |  a[j+1] = ", array[j+1])
    return array


a = [3,4,5,1,6,8,7,9,2]
print("The maximum number in the array is ", max(a))
print("The location of the searched item with linear is ", linearSearch(a, 6))
print("The location of the searched item is ", binarySearch(a, 5))

a = [3, 4, 5, 1, 6, 8, 7, 9, 2]
print("\noriginal array is ", a)
print("sorted array using bubble sort is ", bubbleSort(a))
