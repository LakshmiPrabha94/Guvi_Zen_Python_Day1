#Name: Lakshmi Prabha
#Program : Write a program that takes two strings and returns the longest common substring between them 
#Version: 1
#Programming Language : Python
#Python Version: 3.12.0

def longest_common_substring(str1, str2):

    # Initialize variables to store the length of the common substring
    max_length = 0
    # Initialize a variable to store the starting index of the common substring
    start_index = 0

    # Iterate through each character in the first string
    for i in range(len(str1)):
        # Iterate through each character in the second string
        for j in range(len(str2)):
            # Initialize a variable to store the length of the common substring at the current position
            length = 0
            # Iterate while characters match and we are within the bounds of both strings
            while (i + length < len(str1) and
                   j + length < len(str2) and
                   str1[i + length] == str2[j + length]):
                length += 1

            # Update the longest common substring information if needed
            if length > max_length:
                max_length = length
                start_index = i

    # Return the longest common substring
    return str1[start_index:start_index + max_length]


# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = longest_common_substring(string1, string2)

# Display the result
if result:
    print("Longest Common Substring:", result)
else:
    print("No common substring found.")
