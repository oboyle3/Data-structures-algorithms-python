'''
write a function to determine if the array passed is sorted

Function is_sorted(array):
    #loop through array
    for i from 0 to length of array -2:
        if array[i] > array[i +1]
            retrun false
    return true

'''
def is_sorted(arr):
    #loop through array
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            print(f"this array is not sorted form least to greatest: {arr[i]} is greater than {arr[i+1]}")
            return False
    return True

sample = [1,2,3,8,2]
print(is_sorted(sample))

sample2 = [2,3,5,6,82]
print(is_sorted(sample2))
