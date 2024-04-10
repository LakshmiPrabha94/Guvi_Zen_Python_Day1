#Name: Lakshmi Prabha
#Program : Count the no. of words in a given string.
#Date : 25 Nov 2023
#Version: 1
#Python Version: 3.12.0

def count_words(input_string):
   # Split the input string into a list of words using whitespace as the delimiter
    words = input_string.split()

    # Count the number of words in the list
    word_count = len(words)

    return word_count

# Get input from the user
print()
input_string = input("Enter a string: ")
result = count_words(input_string)
# Display the result
print()
print("Number of words in the string: ", end="")
print(result)
print()
