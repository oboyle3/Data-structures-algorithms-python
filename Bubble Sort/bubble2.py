#sort this array arr = [90, 80, 12, 3]

def the_bub(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [90, 80, 12, 3]
print(f"un sorted {arr}")
print(f"sorted :")
#the_bub(arr)
print(the_bub(arr))