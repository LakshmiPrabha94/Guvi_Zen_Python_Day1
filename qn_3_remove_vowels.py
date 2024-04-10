#Name: Lakshmi Prabha
#Program : Remove the vowels in a given string and return new string with no vowels.
#Date : 25 Nov 2023
#Version: 1
#Python Version: 3.12.0

def remove_vowels(input_string):

    vowels = "aeiouAEIOU"
    
    # Initialize an empty string to store the result
    result_string = ""

    # Iterate through each character in the input string using a for loop
    for char in input_string:
        # Check if the character is not a vowel
        if char not in vowels:
            # Add the non-vowel character to the result string
            result_string += char

    return result_string

# Get input from the user
input_string = input("Enter a string: ")
result = remove_vowels(input_string)

# Display the result - Print the original and processed text
print()
print("Original text: " + input_string)
print("Text with vowels removed: " + result)
print()
