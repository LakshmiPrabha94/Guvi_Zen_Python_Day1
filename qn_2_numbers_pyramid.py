#Name: Lakshmi Prabha
#Program : Create a pyramid of numbers from 1 to 20.
#Date : 25 Nov 2023
#Version: 1
#Python Version: 3.12.0

# Define the height of the pyramid
pyramid_height = 20 

# Outer loop for each row
for i in range(1, pyramid_height + 1): 
    # Inner loop for each column in the row
    for j in range(1, i + 1):
        # Print the current number with a space
        print(j, end=" ")
        
    # Move to the next line after printing each row
    print()


