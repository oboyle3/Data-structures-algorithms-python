

def palin(s):
    length = len(s)
    print(f"the length of the given string is {length}")
    for i in range(length // 2):#only need to check till middle
        left_side = s[i]
        right_side = s[length -1 -i]
        print(f"left side = {left_side} || right side = {right_side}")


somestring = "hello world"
print(palin(somestring))