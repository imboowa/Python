numbers = [4,1,0,5,2,9,6,8,7,3]
size = len(numbers)

def bubbleSort(array, size):
    for i in range(size - 1):
        for j in range(size - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

def printArray(array, size):
    for i in range(size):
        print(array[i],end=" ")

bubbleSort(numbers, size)
printArray(numbers, size)
print()
