def sum_even_num(arr):
    #make the sum equal to zero
    sum = 0

    for num in arr:
        print(f"current sum: {sum}")
        if num % 2 == 0:
            sum = num + sum
    return sum
            


test_array = [1,2,3,4,5,6]
print(sum_even_num(test_array))

'''
psedo code
def sum_event_num(arr):
    intialize current_sum as first num in array
    loop through array:
    if number is even 
        add num to sum
    return sum
'''