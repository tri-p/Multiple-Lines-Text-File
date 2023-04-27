# PABUNA, KATRINA B. 
# Write a method in python to write multiple line of text contents into a text file mylife.txt

# Open mylife.txt (append)
with open("mylife.txt", "a") as output_lines:
    # Use a loop to repeat the process until it becomes false
    while True:
        # Ask the user to enter a line
        line = input("Enter line: ")
        # Write the line onto the text file
        output_lines.write(line + "\n")
        # Ask the user if there are more lines
        more_line = input("Are there more lines (y/n)? ").lower()
        # If no, end the loop
        if more_line == "n":
            break
        # If the user entered an invalid answer, print 'error'
        elif more_line.lower() != 'y':
            print("Error: Invalid input. Please enter 'y' or 'n'.")