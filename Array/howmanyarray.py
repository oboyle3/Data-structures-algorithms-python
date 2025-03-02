'''
write a function that tells you how many times a target number is in a array
'''

def how_many_occurance(arr, target):
    counter = 0
    for num in arr:
        if num == target:
            counter = counter + 1
    return counter

sample = [1,3,73,5,9,8,5,1]
target = 1
print(f"the amount of times the target: {target} occures in this array is {how_many_occurance(sample, target)}")
