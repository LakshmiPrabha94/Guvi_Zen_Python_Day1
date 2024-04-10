#Name: Lakshmi Prabha
#Program : Program that takes a string and returns the most frequent characters in it.
#Date : 25 Nov 2023
#Version: 1
#Python Version: 3.12.0

def most_frequent_characters(input_string):
    # Initialize variables to keep track of the most frequent character(s)
    max_frequency = 0
    frequent_characters = ""

    # Iterate through each character in the input string using a for loop
    for char in input_string:
        # Initialize a counter for the current character's frequency
        current_frequency = 0

        # Iterate through the entire string to count the frequency of the current character
        for other_char in input_string:
            if char == other_char:
                current_frequency += 1

        # Update the most frequent character(s) if needed
        if current_frequency > max_frequency:
            max_frequency = current_frequency
            frequent_characters = char
        elif current_frequency == max_frequency and char not in frequent_characters:
            frequent_characters += char

    return frequent_characters

# Get the input string from the User.
print()
input_string = input("Enter a string: ")
result = most_frequent_characters(input_string)

# Display the result
print("Most frequent character(s) in the string: " + result)
print()
