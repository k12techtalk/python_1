#this code imports a csv of all used usernames and then checks input against
#said csv file

#import the csv module
import csv

#open the csv file
f = open('userNames.csv')

#read the csv file
csv_f = csv.reader(f)

#create variable to inject csv into for a list
usrNames = []

#user to input username to be checked
checkName1 = input('Enter Username to check:')

#insert used usernames from csv into var usrNames as a list
for row in csv_f:
	usrNames.append(row[0])

#check inputed username against list from csv and do one of two actions
if any(checkName1 in s for s in usrNames):
	print("found");
else:
	print("not found")

#close csv file (must be done after open)
f.close()