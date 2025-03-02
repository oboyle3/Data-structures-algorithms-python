#caluslates the sum of array

def sum_arr(arr):
    #set current sum = 0
    current_sum = 0

    #loop though the array and add the current elemnet to the current sum
    for num in arr:
        print(f"num = {num}")
        current_sum = current_sum + num
    return(current_sum)


numbers = [2,3,7]
print(sum_arr(numbers))