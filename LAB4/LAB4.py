# Finding the maximum number in an array:
def max(a):
    max = a[0]
    for i in range(1, len(a)):
        if max < a[i]:
            max = a[i]
    return max

# Linear Search:

# Binary Search:

# Bubble Sort:



a = [3,4,5,1,6,8,7,9,2]
print("The maximum number in the array is ", max(a))
print("The location of the searched item with linear is ", linearSearch(a, 6))
print("The location of the searched item is ", binarySearch(a, 5))

a = [3, 4, 5, 1, 6, 8, 7, 9, 2]
print("original array is ", a)
print("sorted array using bubble sort is ", bubbleSort(a))
