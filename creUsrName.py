#this code is a test of creating usernames from first and last name fields

fname = input("Please enter user's first name: ")
lname = input("Please enter user's last name: ")

uname = fname[0] + lname

#this code gives a clear screen at the bottom of terminal window
print(chr(27) + "[2J")

#this code capitalizes both first and last name and then returns twice
print("Your full name is:", fname.capitalize(), lname.capitalize(),"\n\n")

#this code returns primary username in lowercase
print("Your username is:", uname.lower())

#this code returns an alternative username by adding the "2" as 
#part of the string
print("Your alternate username is:", uname.lower()+"2")

#this code returns username concatinated with @op97.org and 
#three return lines
print("Your email address is:", uname.lower()+"@op97.org\n\n\n")
