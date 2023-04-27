# PABUNA, KATRINA B. 
# Write a method in python to write multiple line of text contents into a text file mylife.txt

# Open mylife.txt (append)
with open("mylife.txt", "a") as output_lines:
    # Use a loop to repeat the process until it becomes false
    while True:
        # Ask the user to enter a line
        print("\n", "\033[93m=" * 80, "\n")
        line = input("\033[92mEnter line: \033[97m")
        # Write the line onto the text file
        output_lines.write("=" * 80 + "\n" + line + "\n")
        # Ask the user if there are more lines
        print("\n", "\033[93m=" * 80, "\n")
        more_line = input("\033[96mAre there more lines (y/n)? \033[97m").lower()
        # If no, end the loop
        if more_line == "n":
            print("\n", "\033[93m=" * 80, "\n")
            output_lines.write("=" * 80 + "\n")
            break
        # If the user entered an invalid answer, print 'error'
        elif more_line.lower() != 'y':
            print("\033[91mError: Invalid input. Please enter 'y' or 'n'.")