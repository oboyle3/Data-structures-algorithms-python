

def bubble(arr):
    for i in range(len(arr)):
        for j in range( len(arr) -i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble(arr))