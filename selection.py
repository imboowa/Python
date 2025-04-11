nums = [4,1,7,9,5,2,6,8,3,0]
size = len(nums)

def selectionSort(array, size):
    for i in range(size - 1):
        small_num = i
        for j in range(i + 1, size):
            if array[j] < array[small_num]:
                small_num = j
        array[small_num], array[i] = array[i], array[small_num]

def printArray(array, size):
    for i in range(size):
        print(array[i], end=' ')

selectionSort(nums, size)
printArray(nums, size)
print()
