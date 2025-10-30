# Ask the user for the number of rows for the pattern
num_rows = int(input("Please enter the number of rows: "))

# Use an outer loop for the rows
for i in range(1, num_rows + 1):
    # Use an inner loop for the elements in each row
    for j in range(1, i + 1):
        # Print the numbers separated by spaces without a new line
        print(j, end=' ')
    # Move to the next line to start a new row
    print()
