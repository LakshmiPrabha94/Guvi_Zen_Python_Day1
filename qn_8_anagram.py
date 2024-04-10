#Name: Lakshmi Prabha
#Program : Program that takes a string and returns true if it is an anagram of another string false otherwise.
#Date : 25 Nov 2023
#Version: 1
#Python Version: 3.12.0

def anagrams(str1, str2):
    # Convert both strings to lowercase for case-insensitive comparison
    str1 = str1.lower()
    str2 = str2.lower()

    # Check if the sorted characters of both strings are the same
    if sorted(str1) == sorted(str2):
        print("True")
    else:
        print("False")

# Get input from the User
print()
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Display the result
result = anagrams(string1, string2)

