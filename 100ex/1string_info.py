name = "Oscar"

print(len(name))                     # Print the length of the string
print(name.find("s"))                # Print the index of the character in the string
name.capitalize()                    # Capitalize the first letter of string
name.upper()                         # Set string to all uppercase
name.lower()                         # Set all characters to lowercase
name.isdigit()                       # Checks if string is ALL digits returns a boolean
name.isalpha()                       # Checks if string is ALL letters returns a boolean
name.count("s")                      #Returns how many times there is a character in string
name.replace("a" , "o")  #Changes all characters for another character

print(name*3)                        #Multiply the display of the string