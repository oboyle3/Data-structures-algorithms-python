def is_palindrome(s):
    # Normalize the string: convert to lowercase and remove spaces, commas, and periods
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    print(f"Normalized string: {s}")  # Debug print

    length = len(s)  # Get the length of the string
    print(f"String length: {length}")  # Debug print

    # Loop through the first half of the string
    for i in range(length // 2):
        left_char = s[i]  # Character from the left side
        right_char = s[length - 1 - i]  # Corresponding character from the right side

        # Print the comparison happening at each step
        print(f"Comparing: {left_char} (left) vs {right_char} (right)")

        if left_char != right_char:
            print("Characters do not match. Not a palindrome.")
            return False  # If any pair doesn't match, it's not a palindrome
    
    print("All characters matched. It's a palindrome!")
    return True  # If loop completes, it's a palindrome

# Test cases
print(is_palindrome("racecar"))  # True
