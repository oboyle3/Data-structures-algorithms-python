#write a function to sort this array : some_list = [30, 10, 88, 82, 70]

def bubble_sort(some_array):
    n = len(some_array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if some_array[j] > some_array[j+1]:
                some_array[j], some_array[j+1] =  some_array[j+1], some_array[j]
    return some_array

some_list = [30, 10, 88, 82, 70]
print(f"Before sorted: {some_list}")
print(f"--WAITING--")
print(bubble_sort(some_list))