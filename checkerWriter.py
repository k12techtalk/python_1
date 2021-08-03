#this code imports a csv of all used usernames and then checks input against
#said csv file. If not found it will add the checked username

#import the csv module
import csv

#open the csv file
f = open("userNames1.csv", "r+")

#read the csv file
csv_f = csv.reader(f)

write_f = csv.writer(f)

#create variable to inject csv into for a list
usrNames = []

#user to input username to be checked
checkName1 = input('Enter Username to check:')

#insert used usernames from csv into var usrNames as a list
for row in csv_f:
	usrNames.append(row[0])

#check inputed username against list from csv and do one of two actions
if any(checkName1 in s for s in usrNames):
	print("Username already used");

#if the username was not found it will add the username to the CSV and 
#tell user that the username was not found and was added to the file
else:
	write_f.writerow([checkName1])
	print("Username available and marked as used")

#close csv file (must be done after open)
f.close()