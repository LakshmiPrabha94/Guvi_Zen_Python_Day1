#Name: Lakshmi Prabha
#Program : Count the total number of vowels and individual vowel counts in a given string.
#Date : 25 Nov 2023
#Version: 1
#Python Version: 3.12.0


def count_vowels(string):

    # Initialize counts
    total_vowels = 0                                        
    a_count = e_count = i_count = o_count = u_count = 0
    
    # Iterate through characters in the string
    for char in string:
        lowercase_char = char.lower()
        if lowercase_char in 'aeiou':
            total_vowels += 1
            if lowercase_char == 'a':
                a_count += 1
            elif lowercase_char == 'e':
                e_count += 1
            elif lowercase_char == 'i':
                i_count += 1
            elif lowercase_char == 'o':
                o_count += 1
            elif lowercase_char == 'u':
                u_count += 1
    
    return total_vowels, a_count, e_count, i_count, o_count, u_count

# Given string
input_string = "Guvi Geeks Network Private Limited"

# Get results
total_vowels, a_count, e_count, i_count, o_count, u_count = count_vowels(input_string)

# Display results
print("Total vowels:", total_vowels)
print("Individual vowel counts:")
print("A:", a_count)
print("E:", e_count)
print("I:", i_count)
print("O:", o_count)
print("U:", u_count)
