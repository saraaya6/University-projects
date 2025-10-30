# Prompt the user to enter a string
input_string = input("Please enter a string: ")

# Create a new string to store the reversed string
reversed_string = ""

# Reverse the string by iterating through the characters in reverse order and appending them to the reversed string
for char in input_string[::-1]:
    reversed_string += char

# Print the reversed string
print("Reversed string:", reversed_string)
