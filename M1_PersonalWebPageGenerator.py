#   Author: Sam
#   Date: 03-18-2023
#   Description: Personal Web Page Ganerator
#                   This program prompts the user for her/his name 
#                       and a sentence that describes herself or himself,
#                       then is creates an HTML file, containing the input for a simple Web page.                       


# COncatenates two strings
def concatenate_string(string1, string2):
    position = string1.find(string2)
    if (position < 0):
        string1 += string2
    return string1

# Prompt user for name and description of herself/himself
name = input("Enter your name: ")
description = input("Descrcibe yourself in a sentence: ")

# Asign filename
filename = name + ".html"

# Open file with mode writing
outfile = open(filename, 'w')

escape_n = "\n"

# Write to file
line = "<html>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "<head>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "</head>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "<body>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "    <center>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "        <h1>" + name + "</h1>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "    </center>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "    <hr />"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "    " + description
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "    <hr />"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "</body>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

line = "</html>"
line = concatenate_string(line, escape_n)
outfile.write(f"{line}")

# Close file
outfile.close()

print(f"The file {filename} has been created.")