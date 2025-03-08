arr = [10, 7, 18, 13]
n = len(arr)

for i in range(n):
         # Inner loop to compare adjacent elements
    for j in range(0, n - i - 1):
        #print(f"({i}, {j})"
        if arr[j] > arr[j+1]:
            print(f"arr j = {arr[j]}  AND  arr j + 1 = {arr[j+1]} We detetcted a swap opportunity")
            print(f"lets swap {arr[j]}  AND {arr[j+1]}")
            #arr[j], arr[j+1] = arr[j+1], arr[j]
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"new array with the change {arr}")


        #print(f"in poistion i: {i} is '{arr[i]}'")
        #print(f"in poistion j: {j} is '{arr[j]}'")
